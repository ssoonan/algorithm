class Node {
  int data;
  Node next;

  public Node(int data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  Node head;

  public LinkedList() {
    this.head = null;
  }

  // 맨 뒤에 넣음
  public void insert(int data) {
    Node newNode = new Node(data);
    if (this.head == null) {
      this.head = newNode;
      return;
    }
    // head에서 시작, 이후 계속 넘어가다 null이면 그 뒤에 박아버림
    Node nextNode = this.head;
    while (nextNode.next != null) {
      nextNode = nextNode.next;
    }
    nextNode.next = newNode;
  }

  // 맨 앞에 넣음
  public void push(int data) {
    Node newNode = new Node(data);
    if (this.head == null) {
      this.head = newNode;
      return;
    }
    Node temp;
    temp = this.head;
    this.head = newNode;
    this.head.next = temp;
  }

  public void display() {
    Node current = head;
    while (current != null) {
      System.out.print(current.data + " ");
      current = current.next;
    }
    System.out.println('\n');
  }

  public static void main(String[] args) {
    LinkedList a = new LinkedList();
    a.insert(5);
    a.insert(6);
    a.insert(65);
    a.push(12);
    a.display();

    // Node a = new Node(1);
    // a.next = new Node(2);
  }
}