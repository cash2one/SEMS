# author: HuYong
#coding=utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

from wechat import wechat_index,wechatViews

urlpatterns = [
    url(r'^wechat_index$',wechat_index.index),
    url(r'^index$', wechatViews.index),
    url(r'^regist$',wechatViews.regist),
    url(r'^doregist$',wechatViews.doregist),
    url(r'^bind$',wechatViews.bind),
    url(r'^state$',wechatViews.state),
    url(r'^control$',wechatViews.control),
    url(r'^history$',wechatViews.history),
    url(r'^nearby$',wechatViews.nearby),
]