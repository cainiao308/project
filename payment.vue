<template>
	<view>
		<page-head :title="title"></page-head>
		<view class="uni-padding-wrap uni-common-mt">
			<view class="uni-btn-v">
				<button type="default" @tap="modalTap">有标题的modal</button>
				<button type="default" @tap="noTitlemodalTap">无标题的modal</button>
			</view>
		</view>
	</view>
</template>
<script>

	export default {
		data() {
			return {
				title: 'modal',
				modalHidden: true,
				modalHidden2: true,
				providerList:[]
			}
		},
		onLoad() {
			uni.getProvider({
				service: 'share',
				success: (result) => {
					console.log(result)
					this.providerList = result.provider.map((value) => {
						let providerName = '';
						switch (value) {
							case 'weixin':
								providerName = '微信登录'
								break;
							case 'qq':
								providerName = 'QQ登录'
								break;
							case 'sinaweibo':
								providerName = '新浪微博登录'
								break;
							case 'xiaomi':
								providerName = '小米登录'
								break;
							case 'alipay':
								providerName = '支付宝登录'
								break;
							case 'baidu':
								providerName = '百度登录'
								break;
							case 'toutiao':
								providerName = '头条登录'
								break;
						}
						return {
							name: providerName,
							id: value
						}
					});
		
				},
				fail: (error) => {
					console.log('获取登录通道失败', error);
				}
			});
		},
		methods: {
			async modalTap(e) {
				// uni.showModal({
				// 	title: "弹窗标题",
				// 	content: "弹窗内容，告知当前状态、信息和解决方法，描述文字尽量控制在三行内",
				// 	showCancel: false,
				// 	confirmText: "确定"
				// })
				let orderInfo = await this.getOrderInfo();
				console.log("得到订单信息", orderInfo);
				if (orderInfo.statusCode !== 200) {
				    console.log("获得订单信息失败", orderInfo);
				    uni.showModal({
				        content: "获得订单信息失败",
				        showCancel: false
				    })
				    return;
				}
				uni.requestPayment({
				    provider: "alipay",
				    orderInfo: orderInfo.data,
				    success: (e) => {
				        console.log("success", e);
				        uni.showToast({
				            title: "感谢您的赞助!"
				        })
				    },
				    fail: (e) => {
				        console.log("fail", e);
				        uni.showModal({
				            content: "支付失败,原因为: " + e.errMsg,
				            showCancel: false
				        })
				    },
				    complete: () => {
				        this.providerList[index].loading = false;
				    }
				})
				
			},
			getOrderInfo(e) {
			    let appid = "";
			    // #ifdef APP-PLUS
			    appid = plus.runtime.appid;
			    // #endif
				let url ='http://10.90.94.155:8888/test';
			    return new Promise((res) => {
			        uni.request({
			            url: url,
			            success: (result) => {
			                res(result);
			            },
			            fail: (e) => {
			                res(e);
			            }
			        })
			    })
			},
			
		}
	}
</script>
