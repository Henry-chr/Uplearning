// pages/logon/logon.js
var app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user_name:null,
    user_pwd:null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  },

  usernameinput: function (event) {
    console.log(event.detail.value)
    this.setData({user_name:event.detail.value})
  },

  passwordinput: function (event) {
    console.log(event.detail.value)
    this.setData({user_pwd:event.detail.value})
  },

  loginBtnClick: function () {
    app.appData.userInfo = {user_name:this.data.user_name,password:this.data.user_pwd}
    console.log(app.appData.userInfo)
    wx.switchTab({
      url: '../user/user',
      success:function(res){
        console.log(res)
      }
    })
  }
})