import re
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error

from utils.config import Config
from utils.log import logger


class Email:
    def __init__(self, message=None, path=None):
        """
        初始化Email
        :param server: smtp服务器，必填
        :param port: SSL服务器端口，smtp.qq.com，使用SSL，端口号465或587
        :param sender: 发件人，必填
        :param password: 发件人密码，必填
        :param receiver: 收件人，多个收件人用“；”隔开，必填
        :param title: 邮件标题，必填
        :param message: 邮件正文，非必填
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填
        """
        c = Config().get('mail')
        self.title = c.get('title')
        self.server = c.get('server')
        self.port = c.get('port')
        self.sender = c.get('sender')
        self.password = c.get('password')
        self.receiver = c.get('receiver')
        self.files = path
        self.message = message
        self.msg = MIMEMultipart("related")

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEApplication(open(att_file, 'rb').read())     # 这里使用MIMEApplication支持多种格式作为附件
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        if self.message:
            self.msg.attach(MIMEText(self.message))

        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        try:
            smtp_server = smtplib.SMTP_SSL(self.server, self.port)
        except (gaierror and error) as e:
            logger.exception("发送邮件失败，无法连接到SMTP服务器，检查网络及SMTP服务器。%s", e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('用户名密码验证失败!%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
                logger.info('发送邮件"{0}"成功！ 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))
            finally:
                smtp_server.quit()


if __name__ == '__main__':
    e = Email(path=r'E:\pythonScript\Report_B\20171101090936result.html')
    e.send()
