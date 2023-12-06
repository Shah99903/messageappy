class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender

class Publisher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish_message(self, content, sender):
        message = Message(content, sender)
        for subscriber in self.subscribers:
            subscriber.receive_message(message)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive_message(self, message):
        print(f"{self.name} received a message from {message.sender}: {message.content}")



if __name__ == "__main__":
    publisher = Publisher()

    subscriber1 = Subscriber("Subscriber1")
    subscriber2 = Subscriber("Subscriber2")

    publisher.add_subscriber(subscriber1)
    publisher.add_subscriber(subscriber2)

    publisher.publish_message("Hello World!", "Publisher")

