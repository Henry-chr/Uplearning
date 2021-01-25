
var app = getApp();
// pages/user/user.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    username:null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    if (app.appData.userInfo == null){
      // 没有用户信息不能返回用户界面
      // wx.navigateTo({
      //   url: '../logon/logon',
      // })
      wx.redirectTo({
        url: '../logon/logon',
      })
    }
    else{
      // console.log(app.appData.userInfo)
      // console.log(app.appData.userInfo.user_name)
      // console.log(app.appData.userInfo.password)
      this.setData({username:app.appData.userInfo.user_name})
    }

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})