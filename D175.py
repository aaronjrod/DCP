import random

def next_child(children):
    prob = random.random()
    total_prob = 0
    for child in children:
        total_prob += child[1]
        if total_prob > prob:
            return child[0]

def sim_markov(start, transition_prob, num_steps):
    node_dict = {}
    visit_dict = {}
    for tuple in transition_prob:
        node_val = tuple[0]
        if node_val not in node_dict:
            node_dict[node_val] = []
            visit_dict[node_val] = 0
        node_dict[node_val].append((tuple[1], tuple[2]))
    
    node = start
    for i in range(num_steps):
        visit_dict[node] += 1
        node = next_child(node_dict[node])
    return visit_dict

transition_prob= [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
print(sim_markov('a', transition_prob, 5000))