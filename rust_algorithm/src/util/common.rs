pub struct Node {
  pub item: i32,
  pub prev: Option<Box<Node>>,
  pub next: Option<Box<Node>>,
}

impl Node {
  pub fn new(item: i32) -> Node {
    Node {
      item,
      prev: None,
      next: None,
    }
  }
  // 다른 것보다 Box로 감싼다는 걸 잊고 있었음
  pub fn set_next(&mut self, next_node: Node) {
    self.next = Some(Box::new(next_node));
  }
  pub fn set_prev(&mut self, prev_node: Node) {
    self.prev = Some(Box::new(prev_node)); // Box로 감싸서 prev에 저장
  }
}

impl Clone for Node {
  fn clone(&self) -> Self {
    Node {
      item: self.item, // i32는 Copy 트레이트를 구현하므로 바로 복사 가능
      prev: self.prev.as_ref().map(|prev| Box::new((**prev).clone())), // prev를 재귀적으로 복제
      next: self.next.as_ref().map(|next| Box::new((**next).clone())), // next를 재귀적으로 복제
    }
  }
}
