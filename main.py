import string

class Node:
    def __init__(self, key=None): self.key = key; self.prev = self.next = None
    def set_key(self, key): self.key = key

class LinkedList:
    def __init__(self): self.head = self.tail = None; self.size = 0
    def add(self, node):
        if self.head is None: node.next = node.prev = node; self.head = node; self.tail = self.head
        else: node.prev = self.tail; self.tail.next = self.head.prev = node; node.next = self.head; self.tail = node
        self.size += 1
    def get(self, pos):
        curr = self.head
        for _ in range(pos): curr = curr.next
        return curr
    def remove(self, key):
        head = self.head
        if head is None: return None
        curr, prev = head, None
        while curr.key != key: prev = curr; curr = curr.next
        if curr == head and curr.next == head: head = None; return None
        if curr == head:
            prev = head
            while prev.next != head: prev = prev.next
            head = curr.next; prev.next = head
        elif curr.next == head: prev.next = head
        else: prev.next = curr.next
        self.size -= 1; return prev

def build(n):
    ret = LinkedList()
    for i in range(n): ret.add(Node(string.ascii_uppercase[i]))
    return ret

def main():
    n, m, o = map(int, input().split()); l, r = build(n), []; s = l.get(m); i = s; a = i.key; s.set_key(None); i = i.next;
    while l.size != 1:
        c = 1
        while c < o:
            if i.next.key is None: i = i.next; continue
            i = i.next; c += 1
        t = l.remove(i.key); b = i.key; i = t.next
        while 1:
            if i.key is None and t.key is None: r.append(b); i = i.next; break
            if i.key is None: r.append(a); i, a = t, b; break
            if t.key is None: r.append(b); break
            i, t = i.next, t.prev
    r.append(a); return r

if __name__ == "__main__":
    ans = main()
    for i in ans[:-1]: print("{} escaped!".format(i))
    print("{} is the loser!".format(ans[-1]))
