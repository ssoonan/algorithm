struct Node {
    item: i32,
    next: Option<Box<Node>>,
}

impl Node {
    fn new(item: i32, next: Option<Box<Node>>) -> Node {
        Node { item, next }
    }
}

struct Stack {
    last: Node,
}

impl Stack {
    fn new() {}
    fn push() {}
    // fn pop() -> Node {}
}

fn main() {
    let node1 = Node::new(5, None);
    let node2 = Node::new(10, Some(Box::new(node1)));
    let node3 = Node::new(7, Some(Box::new(node2)));

    // 리스트 출력
    let mut current = Some(Box::new(node3));
    while let Some(node) = current {
        println!("{}", node.item);
        current = node.next;
    }
}
