module.exports = (function() {

    // TODO: use prepared statements

    var utils = require('./utils');
    var cassandra = require('cassandra-driver');
    var cassandraClient = new cassandra.Client({contactPoints: ['cassandrahost'], keyspace: 'biketimer'});
    var facebookFacade = require('./facebook_facade');

    function getFbUserExistsQuery(fbId){
        return "select count(1) " + 
                "from users " + 
                "where fb_id='" + fbId + "' " +
                "allow filtering";
    };
    
    function  getFbUserQuery(fbId){
        return "select id, fb_id, email, bt_name, fb_access_token, fb_name, fb_surname " +
                "from users " +
                "where fb_id='" + fbId + "' " +
                "allow filtering";
    };
    
    function getInsertFbUserCommand(userData, friendsBtIdsList){
        var i, friendsIdsStringList;
        for(i = 0; i < friendsBtIdsList.length; ++i){
            friendsBtIdsList[i] = ("" + friendsBtIdsList[i] + "");
        }
        friendsIdsStringList = friendsBtIdsList.join(", ")
        
        return "insert into users (id, fb_id, email, bt_name, fb_access_token, fb_name, fb_surname, friends_ids, roles) " + 
                "values (" +
                "" + userData.id + ", " +
                "'" + userData.fbId + "', " +
                "'" + userData.email + "', " +
                "'" + (userData.fbName + " " + userData.fbSurname) + "', " +
                "'" + userData.fbAccessToken + "', " +
                "'" + userData.fbName + "', " +
                "'" + userData.fbSurname + "', " +
                "[" + friendsIdsStringList + "], " +
                "['biker'])";
    }
    
    function getAddFriendCommand(usersToUpdateBtIds, newFriendBtId){
        var usersToUpdateBtIdsString = usersToUpdateBtIds.join(", ");
        return "update users " +
               "set friends_ids = friends_ids + [" + newFriendBtId + "] " +
               "where id in (" + usersToUpdateBtIdsString + ");"
    }

    function userExists(userData, onUserExistsSuccess, onUserExistsError){

        var fbUserExistsQuery;
        if(!userData || !userData.fbId){
            onUserExistsError('application_error', 'No user fbId provided.');
        }

        fbUserExistsQuery = getFbUserExistsQuery(userData.fbId);
        cassandraClient.execute(fbUserExistsQuery, function (err, result) {
            console.log('Cassandra query: ' + fbUserExistsQuery + ' err: ' + err + ' result: ' + result);
            if (!err){
                if(result.rows.length == 1){
                    console.log('Cassandra query: ' + fbUserExistsQuery + ' result.rows.length: ' + result.rows.length);
                    if(!isNaN(result.rows[0].count)){
                        var numberOfUsers = parseInt(result.rows[0].count);
                        console.log('Cassandra query: ' + fbUserExistsQuery + ' users count: ' + result.rows[0].count);
                        if(numberOfUsers === 0){
                            onUserExistsSuccess(false);
                        }else if(numberOfUsers === 1){
                            onUserExistsSuccess(true);
                        }else{
                            onUserExistsError('db_data_error', 'More than 1 users found for given FB id.');
                        }
                    }else{
                        onUserExistsError('db_data_error', 'Cannot parse query result.');
                    }
                }else{
                    onUserExistsError('db_access_error', 'Query results are invalid.');
                }
            }else{
                onUserExistsError('db_access_error', 'Query returned an error: ' + err);
            }
        });
    }

    function getUser(userData, onGetUserSuccess, onGetUserError){
        
        var fbUserQuery;
        if(!userData || !userData.fbId){
            onGetUserError('application_error', 'No user fbId provided.');
        }
        
        fbUserQuery = getFbUserQuery(userData.fbId);
        cassandraClient.execute(fbUserQuery, function (err, result) {
            console.log('Cassandra query: ' + fbUserQuery + ' err: ' + err + ' result: ' + result);
            if (!err){
                if (result.rows.length === 1) {
                    onGetUserSuccess({
                        id: result.rows[0].id.toString(),
                        fbId: result.rows[0].fb_id,
                        email: result.rows[0].email,
                        btName: result.rows[0].bt_name,
                        fbAccessToken: result.rows[0].fb_access_token,
                        fbName: result.rows[0].fb_name,
                        fbSurname: result.rows[0].fb_surname
                    });
                }else{
                    onGetUserError('db_data_error', result.rows.length + ' users found for given FB id. Should be exactly 1.')
                }
            }else{
                onGetUserError('db_access_error', 'Query returned an error: ' + err);
            }
        });
    }
    
    function addFriendToUsers(idsOfUsersToUpdate, idOfUserToAdd, onSuccess, onError){
        var addFriendCommand = getAddFriendCommand(idsOfUsersToUpdate, idOfUserToAdd);
        cassandraClient.execute(addFriendCommand, function (err, result) {
            console.log('Cassandra query: ' + addFriendCommand + ' err: ' + err + ' result: ' + result);
            if (!err){
                onSuccess();
            }else{
                onError('db_access_error', 'Query returned an error: ' + err);
            }
        });
    }
    
    function addUser(userData, onAddUserSuccess, onAddUserError){
        
        var friendsCheckedAgainstBtDatabase = 0, friendsBtIds = [];
        
        facebookFacade.getUserFriends(
            userData.fbAccessToken,
            function onGetUserFriendsSuccess(friendsFbIdsList){
                var i, fbUserQuery, insertFbUserCommand;
                if(friendsFbIdsList.data.length > 0){
                    for(i = 0; i < friendsFbIdsList.data.length; ++i){
                        fbUserQuery = getFbUserQuery(friendsFbIdsList.data[i].id);
                        cassandraClient.execute(fbUserQuery, function (err, result) {
                            console.log('Cassandra query: ' + fbUserQuery + ' err: ' + err + ' result: ' + result);
                            if (!err){
                                friendsCheckedAgainstBtDatabase += 1;
                                if (result.rows.length === 1) {
                                    friendsBtIds.push(result.rows[0].id.toString());
                                }
                                if(friendsCheckedAgainstBtDatabase == friendsFbIdsList.data.length){
                                    // TODO: duplication
                                    userData.id = utils.guid();
                                    insertFbUserCommand = getInsertFbUserCommand(userData, friendsBtIds);
                                    cassandraClient.execute(insertFbUserCommand, function (err, result) {
                                        console.log('Cassandra query: ' + insertFbUserCommand + ' err: ' + err + ' result: ' + result);
                                        if (!err){
                                            addFriendToUsers(
                                                friendsBtIds, 
                                                userData.id, 
                                                function() {onAddUserSuccess(userData)},
                                                onAddUserError);
                                        }else{
                                            onAddUserError('db_access_error', 'Query returned an error: ' + err);
                                        }
                                    });
                                }
                            }else{
                                onAddUserError('db_access_error', 'Query returned an error: ' + err);
                            }
                        });
                    }
                }else{
                    // TODO: duplication
                    userData.id = utils.guid();
                    insertFbUserCommand = getInsertFbUserCommand(userData, []);
                    cassandraClient.execute(insertFbUserCommand, function (err, result) {
                        console.log('Cassandra query: ' + insertFbUserCommand + ' err: ' + err + ' result: ' + result);
                        if (!err){
                            addFriendToUsers(
                                friendsBtIds, 
                                userData.id, 
                                function() {onAddUserSuccess(userData)},
                                onAddUserError);
                        }else{
                            onAddUserError('db_access_error', 'Query returned an error: ' + err);
                        }
                    });
                }
            },
            onAddUserError);
    }

    function getOrAddUser(userData, onGetOrAddUserSuccess, onGetOrAddUserError) {
        userExists(userData,
        function onUserExistsSuccess(userExists){
            if(userExists){
                getUser(userData,
                    onGetOrAddUserSuccess,
                    onGetOrAddUserError);
            }else{
                addUser(userData,
                    onGetOrAddUserSuccess,
                    onGetOrAddUserError);
            }
        },
        onGetOrAddUserError);
    };
    
    return {
        getOrAddUser: getOrAddUser
    };

}());