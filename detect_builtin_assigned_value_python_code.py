import ast
import builtins
from this import d

class AssignmentNodeVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.visited_names = []
        super().__init__()
    
    def visit_Assign(self, node):
        if node.targets:
            targets = node.targets
            for target in targets:
                if isinstance(target, ast.Name):
                    self.visited_names.append(target.id)
                elif isinstance(target, ast.Tuple):
                    for elem in target.elts:
                        self.visited_names.append(elem.id)

    def get_invalid_names(self, target_var_names):
        return list(set(target_var_names).intersection(set(self.visited_names)))


class ClassDefNodeVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.visited_names = []
        super().__init__()
        
    def visit_ClassDef(self, node):
        self.visited_names.append(node.name)
    
    def get_invalid_names(self, target_var_names):
        return list(set(target_var_names).intersection(set(self.visited_names)))

class FunctionNodeVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.visited_names = []
        super().__init__()
        
    def visit_FunctionDef(self, node):
        if node.name:
            self.visited_names.append(node.name)
        if node.args:
            for arg in node.args.args:
                self.visited_names.append(arg.arg)
        if node.body:
            # look for nested functions
            for elem in node.body:
                if isinstance(elem, ast.FunctionDef):
                    self.visit_FunctionDef(elem)
                
    def get_invalid_names(self, target_var_names):
        return list(set(target_var_names).intersection(set(self.visited_names)))
    
def find_variable_assignments(source, target_var_names):
      tree = ast.parse(source)
      visitors = [AssignmentNodeVisitor(), FunctionNodeVisitor(), ClassDefNodeVisitor()]
      result = []
      for visitor in visitors:
        visitor.visited_names.clear()
        visitor.visit(tree)
        result.extend(visitor.get_invalid_names(target_var_names))
      return result
  
  
code = """
class str: 
    def __init__(self, list): 
        def next(foo, iter=42, baz=1): bin = 2
"""

print(find_variable_assignments(code, dir(builtins)))