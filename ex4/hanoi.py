from typing import *
import sys


def format_action(name: str, pre: str, add: str, delete: str):
    print(name)
    return f"Name: {name}\npre: {' '.join(pre)} \nadd: {' '.join(add)}\ndelete: {' '.join(delete)}\n"


# def get_sub_orders_helper(seq: List[str], conrainer: Dict[str, List[str]] = dict()):
#     if conrainer.get(str(seq)) is not None:
#         return
#     conrainer[str(seq)] = seq
#     for i in range(len(seq)):
#         get_sub_orders_helper(seq[:i]+seq[i+1:], conrainer)


# def get_sub_orders(seq: List[str]):
#     sub_lists = {}
#     get_sub_orders_helper(seq, sub_lists)
#     sub_lists = list(sub_lists.values())
#     options = []
#     for seq1 in sub_lists:
#         for seq2 in sub_lists:
#             if len(set(seq1) & set(seq2)) == 0:
#                 if len(seq1) > 0 and (len(seq2) == 0 or seq1[-1] < seq2[-1]):
#                     options += [(seq1, seq2)]

#     return sub_lists, options


# def create_domain_file(domain_file_name, n_, m_):
#     disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
#     pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
#     # use domain_file.write(str) to write to domain_file
#     domain_file = open(domain_file_name, 'w')
#     domain_file.write("Propositions:\n")
#     propositions = []
#     actions = []
#     all_sub_lists, options = get_sub_orders(list(range(n_-1, -1, -1)))
#     for src_peg in pegs:
#         for sl in all_sub_lists:
#             propositions += ["_".join([src_peg] + [f'd_{s}' for s in sl])]

#     domain_file.write(' '.join(propositions)+"\n")
#     domain_file.write("Actions:\n")

#     for src_peg in pegs:
#         for des_peg in pegs:
#             if des_peg != src_peg:
#                 for v1, v2 in options:
#                     if len(v1) > 0:
#                         v1 = [f'd_{s}' for s in v1]
#                         v2 = [f'd_{s}' for s in v2]
#                         pre = ["_".join([src_peg] + v1),
#                                "_".join([des_peg] + v2)]
#                         add = ["_".join([src_peg] + v1[:-1]),
#                                "_".join([des_peg] + v2 + [v1[-1]])]
#                         name = "_".join(
#                             ["from", "_".join([src_peg] + v1), "to", "_".join([des_peg] + v2 + [v1[-1]])])
#                         actions += [(name, pre, add, pre)]
#     [domain_file.write(format_action(*action)) for action in actions]
#     domain_file.close()


# def create_problem_file(problem_file_name_, n_, m_):
#     disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
#     pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
#     # use problem_file.write(str) to write to problem_file
#     problem_file = open(problem_file_name_, 'w')
#     problem_file.write(f"Initial state: {"_".join(
#         [pegs[0]]+disks[::-1])} {' '.join(pegs[1:])}\n")
#     problem_file.write(f"Goal state: {"_".join(
#         [pegs[-1]]+disks[::-1])} {' '.join(pegs[:-1])}\n")

# problem_file.close()

def make_prop(x, y): return f'{x}_{y}'


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    # use domain_file.write(str) to write to domain_file
    domain_file = open(domain_file_name, 'w')
    domain_file.write("Propositions:\n")

    propositions = []
    for i in range(n_-1, -1, -1):
        propositions += [make_prop(disks[i], "")]
        for j in range(0, i):
            propositions += [make_prop(disks[i], disks[j])]

    for peg in pegs:
        for disk in disks+[""]:
            propositions += [make_prop(peg, disk)]

    domain_file.write(' '.join(propositions) + "\n")
    domain_file.write("Actions:\n")
    actions = ""
    for i in range(n_):
        for j in range(i+1, n_):
            for k in range(i+1, n_):
                if k != j:
                    pre = [make_prop(disks[i], ""), make_prop(
                        disks[j], ""), make_prop(disks[k], disks[i])]
                    add = [make_prop(disks[j], disks[i]),
                           make_prop(disks[k], "")]
                    delete = [make_prop(
                        disks[j], ""), make_prop(disks[k], disks[i])]
                    name = f"move-disk-{i}-from-disk-{k}-to-disk-{j}"
                    actions += format_action(name, pre, add, delete)
    for p in pegs:
        for i in range(n_):
            for j in range(i+1, n_):
                pre = [make_prop(disks[i], ""), make_prop(
                    p, ""), make_prop(disks[j], disks[i])]
                add = [make_prop(p, disks[i]),
                       make_prop(disks[j], "")]
                delete = [make_prop(
                    p, ""), make_prop(disks[j], disks[i])]
                name = f"move-disk-{i}-from-disk-{j}-to-{p}"
                actions += format_action(name, pre, add, delete)

                pre = [make_prop(disks[i], ""), make_prop(
                    p, disks[i]), make_prop(disks[j], "")]
                add = [make_prop(p, ""),
                       make_prop(disks[j], disks[i])]
                delete = [make_prop(
                    p, disks[i]), make_prop(disks[j], "")]
                name = f"move-disk-{i}-from-{p}-to-disk{j}"
                actions += format_action(name, pre, add, delete)

    for p1 in pegs:
        for p2 in pegs:
            for i in range(n_):
                if p1 != p2:
                    pre = [make_prop(disks[i], ""), make_prop(
                        p1, ""), make_prop(p2, disks[i])]
                    add = [make_prop(p1, disks[i]),
                           make_prop(p2, "")]
                    delete = [make_prop(
                        p1, ""), make_prop(p2, disks[i])]
                    name = f"move-disk-{i}-from-peg-{p2}-to-peg-{p1}"
                    actions += format_action(name, pre, add, delete)
    domain_file.write(actions)
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    # use domain_file.write(str) to write to domain_file
    problem_file = open(problem_file_name_, 'w')
    hip = []
    for i in range(n_-1):
        hip += [make_prop(disks[i+1], disks[i])]
    hip += [make_prop(disks[0], "")]
    hip = ' '.join(hip)

    p_for_initial = [make_prop(peg, "") for peg in pegs[1:]]
    problem_file.write(
        f"Initial state: {make_prop(pegs[0], disks[-1])} {hip} {' '.join(p_for_initial)}\n")
    p_for_goal = [make_prop(peg, "") for peg in pegs[:-1]]
    problem_file.write(
        f"Goal state: {make_prop(pegs[-1], disks[-1])} {hip} {' '.join(p_for_goal)}\n")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
    print(f"python3 graph_plan.py {domain_file_name} {problem_file_name}")
