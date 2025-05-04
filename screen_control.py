from ppadb.client import Client as AdbClient
from PIL import Image
import io
import time

class ScreenControl:
    def __init__(self, host='127.0.0.1', port=5037):
        """初始化ADB客户端连接
        
        Args:
            host: ADB服务器主机地址
            port: ADB服务器端口
        """
        self.client = AdbClient(host=host, port=port)
        self.device = None
        self.connect_device()
    
    def connect_device(self):
        """连接设备，获取第一个可用设备"""
        devices = self.client.devices()
        if not devices:
            raise Exception('没有找到可用的Android设备')
        self.device = devices[0]
    
    def screenshot(self, save_path=None):
        """截取屏幕
        
        Args:
            save_path: 保存截图的路径，如果为None则不保存
            
        Returns:
            PIL.Image对象
        """
        # 获取屏幕截图
        image_data = self.device.screencap()
        # 转换为PIL Image对象
        image = Image.open(io.BytesIO(image_data))
        
        if save_path:
            image.save(save_path)
        
        return image
    
    def tap(self, x, y):
        """点击屏幕指定坐标
        
        Args:
            x: 横坐标
            y: 纵坐标
        """
        self.device.shell(f'input tap {x} {y}')
    
    def swipe(self, start_x, start_y, end_x, end_y, duration=500):
        """滑动屏幕
        
        Args:
            start_x: 起始点横坐标
            start_y: 起始点纵坐标
            end_x: 结束点横坐标
            end_y: 结束点纵坐标
            duration: 滑动持续时间（毫秒）
        """
        self.device.shell(f'input swipe {start_x} {start_y} {end_x} {end_y} {duration}')
    
    def multi_swipe(self, points):
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
            duration = next_point[2] if len(next_point) > 2 else 500
            
            self.device.shell(
                f'input swipe {current_point[0]} {current_point[1]} '
                f'{next_point[0]} {next_point[1]} {duration}'
            )
    def long_press(self, x, y, duration=1000):
        """长按指定坐标
        
        Args:
            x: 横坐标
            y: 纵坐标
            duration: 按住时长（毫秒）
        """
        self.swipe(x, y, x, y, duration)
    
    def input_text(self, text):
        """输入文本
        
        Args:
            text: 要输入的文本
        """
        self.device.shell(f'input text "{text}"')
    
    def press_key(self, keycode):
        """按下指定按键
        
        Args:
            keycode: 按键码，例如3代表HOME键，4代表BACK键
        """
        self.device.shell(f'input keyevent {keycode}')