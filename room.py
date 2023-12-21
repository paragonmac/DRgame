import xml.etree.ElementTree as ET


class clsRoom:
    def __init__(self, room_id):
        tree = ET.parse('Assets/rooms.xml')
        root = tree.getroot()

        room_element = root.find(f'room[@id="{room_id}"]')

        self.id = room_element.attrib['id']
        self.title = room_element('title').text
        self.description = room_element.find('description').text

        self.objects = []
        for obj in root.findall('objects/object'):
            object_id = obj.attrib['id']
            object_name = obj.attrib['name']
            object_description = obj.text
            self.objects.append((object_id, object_name, object_description))

        self.exits = []
        for exit_element in root.findall('exit'):
            exit_direction = exit_element.attrib['direction']
            exit_to = exit_element.attrib['to']
            self.exits.append((exit_direction, exit_to))

    def print_info(self):
        roomID = f"Room ID: {self.id}"
        title = f"Title: {self.title}"
        room_description = f"Description: {self.description}"
        objects = f"Objects: {self.objects}"
        exits = f"Exits: {self.exits}"
        # for exit_info in self.exits:
        # exitlocations[] = (f"  - Direction: {exit_info[0]}, To Room: {exit_info[1]}")
        return roomID, title, room_description, objects, exits

    def update_room(self, *args):
        result = clsRoom.print_info(clsRoom)
        roomID, title, room_description, objects = result
        self.roomwindow.config(state='normal')
        self.roomwindow.insert('end', roomID + '\n')
        self.roomwindow.insert('end', title + '\n')
        self.roomwindow.insert('end', room_description + '\n')
        self.roomwindow.insert('end', objects + '\n')
        self.roomwindow.see('end')
        self.roomwindow.config(state='disabled')
        return result
