from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类


# 注册插件
@register(name="Hello", description="hello world", version="0.1", author="RockChinQ")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if "影子" in msg:  # 如果消息为hello

            # 输出调试信息
            self.ap.logger.info("hello, {}".format(ctx.event.sender_id))

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", ["影子是我儿, {}!".format(ctx.event.sender_id)])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        if "影子" in msg:  # 如果消息为hello

            ctx.add_return("reply", ["龙游贵妇在线扣脚! "])

            ctx.prevent_default()
            

    @handler(NormalMessageResponded)
    async def optimize_message(self, event: EventContext, **kwargs):
        if str(event.event.sender_id) == "1135586980":
            self.ap.logger.info("收到影子的消息")

        original_message = event.event.response_text
        optimized_message = "回我儿子：" + original_message
        if optimized_message:
            event.add_return('reply', optimized_message)
        
        self.ap.logger.info(event.__dict__)        
        self.ap.logger.info(event.event.__dict__)
            

    # 插件卸载时触发
    def __del__(self):
        pass
