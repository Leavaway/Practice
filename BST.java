
//BST iterate
//to find all odd nodes.
public static Integer findOdd(Node node){
		int sum = 0;
		int next = 0;
		if(node.left!=null){
			if(node.left.value%2==1){
				sum+=node.left.value;
			}
			next+=findOdd(node.left);
		}
		if(node.right!=null){
			if(node.right.value%2==1){
				sum+=node.right.value;
			}
			next+=findOdd(node.right);
		}

		return sum+next;
	}
  
  //to fine the sum of the values of all the nodes that have an odd number of direct children.
  public static Integer findOdd(Node node){
		int sum = 0;
		int next = 0;

		if(node.left!=null&&node.right==null){
			sum+=node.value;
			next+=findOdd(node.left);
		}
		if(node.left==null&&node.right!=null){
			sum+=node.value;
			next+=findOdd(node.right);
		}
		if(node.left!=null&&node.right!=null){
			next+=findOdd(node.left)+findOdd(node.right);
		}

		return sum+next;
	}
