class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artits = artist
        self.duration = duration

    def __str__(self):
        return(f'{self.title}, By: {self.artist}, Song Length: {self.duration}')
    
class Node:
    def __int__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
    
    def add_song(self, title, artist, duration):
        new_song = Song(title, artist, duration)
        new_node = Node(new_song)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def remove_song(self, title):
        if self.head is None:
            print('Empty List')
            return
        if self.head.song.title == title:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.song.title == title:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
            print('Song Removed')
        
