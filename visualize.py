import sys
import genotypes
from graphviz import Digraph


def plot_not_relaxed(genotype, filename):
  g = Digraph(
      format='pdf',
      edge_attr=dict(fontsize='20', fontname="times"),
      node_attr=dict(style='filled', shape='rect', align='center', fontsize='20', height='0.5', width='0.5', penwidth='2', fontname="times"),
      engine='dot')
  g.body.extend(['rankdir=LR'])

  g.node("c_{k-2}", fillcolor='darkseagreen2')
  g.node("c_{k-1}", fillcolor='darkseagreen2')
  assert len(genotype) % 2 == 0
  # steps = len(genotype) // 2

  iter0 = 0
  iter1 = 1
  steps = 0
  while iter0+iter1 < len(genotype):
    steps += 1
    iter1 += 1
    iter0 += iter1

  for i in range(steps):
    g.node(str(i), fillcolor='lightblue')

  iter0 = 0
  iter1 = 1
  colors = ["red", "green", "blue", "purple"]
  for i in range(steps):
    # for k in [2*i, 2*i + 1]:
    relax = 0
    for k in range(iter0, iter0+iter1+1):
      relax += 1
      op_best, op_prev_best, j = genotype[k]
      if j == 0:
        u = "c_{k-2}"
      elif j == 1:
        u = "c_{k-1}"
      else:
        u = str(j-2)
      v = str(i)
      if relax <= 2:
        color_k = "red"
      else:
        color_k = "green"
      g.edge(u, v, label=op_best, fillcolor="gray", color=color_k)
      g.edge(u, v, label=op_prev_best, fillcolor="gray", color="blue")
    iter1 += 1
    iter0 += iter1
    relax = 0



  g.node("c_{k}", fillcolor='palegoldenrod')
  for i in range(steps):
    g.edge(str(i), "c_{k}", fillcolor="gray")

  g.render(filename, view=True)


def plot_relaxed(genotype, filename):
  g = Digraph(
      format='pdf',
      edge_attr=dict(fontsize='20', fontname="times"),
      node_attr=dict(style='filled', shape='rect', align='center', fontsize='20', height='0.5', width='0.5', penwidth='2', fontname="times"),
      engine='dot')
  g.body.extend(['rankdir=LR'])

  g.node("c_{k-2}", fillcolor='darkseagreen2')
  g.node("c_{k-1}", fillcolor='darkseagreen2')
  assert len(genotype) % 2 == 0
  # steps = len(genotype) // 2

  iter0 = 0
  iter1 = 1
  steps = 0
  while iter0+iter1 < len(genotype):
    steps += 1
    iter1 += 1
    iter0 += iter1

  for i in range(steps):
    g.node(str(i), fillcolor='lightblue')

  iter0 = 0
  iter1 = 1
  for i in range(steps):
    # for k in [2*i, 2*i + 1]:
    relax = 0
    for k in range(iter0, iter0+iter1+1):
      relax += 1
      op_best, op_prev_best, j = genotype[k]
      if j == 0:
        u = "c_{k-2}"
      elif j == 1:
        u = "c_{k-1}"
      else:
        u = str(j-2)
      v = str(i)
      if relax <= 2:
        color_k = "red"
        g.edge(u, v, label=op_best, fillcolor="gray", color=color_k)
    iter1 += 1
    iter0 += iter1
    relax = 0



  g.node("c_{k}", fillcolor='palegoldenrod')
  for i in range(steps):
    g.edge(str(i), "c_{k}", fillcolor="gray")

  g.render(filename, view=True)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("usage:\n python {} ARCH_NAME".format(sys.argv[0]))
    sys.exit(1)

  genotype_name = sys.argv[1]
  try:
    genotype = eval('genotypes.{}'.format(genotype_name))
  except AttributeError:
    print("{} is not specified in genotypes.py".format(genotype_name)) 
    sys.exit(1)

  plot_not_relaxed(genotype.normal, "normal")
  plot_relaxed(genotype.normal, "normal_r")
  plot_not_relaxed(genotype.reduce, "reduce")
  plot_relaxed(genotype.reduce, "reduce_r")

