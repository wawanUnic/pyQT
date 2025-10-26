import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, Qt

class Ball:
    def __init__(self, color, radius, w, h):
        self.color = QColor(*color)
        self.radius = radius
        self.x = random.randint(radius, w - radius)
        self.y = random.randint(radius, h - radius)
        self.vx = random.choice([-5, -4, -3, 3, 4, 5])
        self.vy = random.choice([-5, -4, -3, 3, 4, 5])

    def move(self, w, h):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.radius < 0 or self.x + self.radius > w:
            self.vx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > h:
            self.vy *= -1

class BallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.setCursor(Qt.BlankCursor)

        screen = QApplication.primaryScreen().geometry()
        self.w, self.h = screen.width(), screen.height()

        self.balls = [
            Ball((255, 0, 0), 40, self.w, self.h),
            Ball((0, 255, 0), 60, self.w, self.h),
            Ball((0, 0, 255), 30, self.w, self.h),
        ]

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0))
        for ball in self.balls:
            ball.move(self.w, self.h)
            painter.setBrush(ball.color)
            painter.drawEllipse(ball.x - ball.radius, ball.y - ball.radius,
                                ball.radius * 2, ball.radius * 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BallWindow()
    sys.exit(app.exec_())
