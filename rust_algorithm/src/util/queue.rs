use super::common::Node;

pub struct Deque {
  pub head: Option<Node>,
  pub tail: Option<Node>,
}

impl Deque {
  pub fn append(&mut self, value: i32) {
    let mut new_node = Node::new(value);

    match self.tail.take() {
      Some(mut old_tail) => {
        new_node.set_prev(old_tail.clone());
        old_tail.set_next(new_node.clone());
        self.tail = Some(new_node);
      }
      None => {
        self.head = Some(new_node);
        self.tail = self.head.clone();
      }
    }
  }
  pub fn appendleft() {}
  pub fn pop() {}
  pub fn popleft() {}
  pub fn peek() {}
  pub fn peepleft() {}

}
