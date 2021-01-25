Page({
  data:{
    switchvalue:null
  },
  formSubmit: function (e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
    this.setData({
      switchvalue:e.detail.value.switch
    })
    console.log(this.data.switchvalue)
    console.log(e.detail.value.switch)
  },
  formReset: function () {
    console.log('form发生了reset事件')
  }
})