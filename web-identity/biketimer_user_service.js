module.exports = (function() {

    function getOrAddUser(userIdInfo, onGetOrAddUserSuccess, onGetOrAddUserError) {
        onGetOrAddUserSuccess({id: '321'});
    };
    
    return {
        getOrAddUser: getOrAddUser
    };

}());