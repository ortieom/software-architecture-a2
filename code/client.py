import cmd
import http.client
import json


server_info = {"host": "127.0.0.1",
               "port": 8000}


def send_message(message):
    conn = http.client.HTTPConnection(**server_info)
    headers = {'Content-Type': 'application/json'}
    body = json.dumps({"message": message})
    conn.request("POST", "/message/", body, headers)
    return conn.getresponse().read().decode()


def get_messages():
    conn = http.client.HTTPConnection(**server_info)
    conn.request("GET", "/messages/")
    messages = json.loads(conn.getresponse().read().decode())
    for i, message in enumerate(messages, start=1):
        yield f"Message {i}: {message['message']} [Posted at {message.get('post_time', '...')}]"


def get_message_count():
    conn = http.client.HTTPConnection(**server_info)
    conn.request("GET", "/messages/count")
    return conn.getresponse().read().decode()


class ChatCli(cmd.Cmd):
    prompt = '> '

    def do_send(self, line):
        """Send a message. Usage: send [your message]"""
        response = send_message(line)
        print(response)

    def do_get(self, line):
        """Get all messages. Usage: get"""
        print('\n'.join(get_messages()))

    def do_count(self, line):
        """Get message count. Usage: count"""
        response = get_message_count()
        print(response)

    def do_quit(self, line):
        """Quit the CLI. Usage: quit"""
        return True


if __name__ == '__main__':
    ChatCli().cmdloop()
