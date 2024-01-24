import random
import matplotlib.pyplot as plt
import numpy as np

children_list = []
version_try = 1.1


def max_and_average_scores(gen_dict):
    if not gen_dict:
        return None

    max_fitness_child = max(gen_dict, key=lambda x: x['fitness'])['fitness']
    avg_fitness = sum(child['fitness'] for child in gen_dict) / len(gen_dict)

    print('max_fitness_child', max_fitness_child, 'avg_fitness', avg_fitness)


def mutate_list(to_be_mutated_list):
    for i in range(0,len(to_be_mutated_list)):
        random_alel=random_binary_list(1)
        to_be_mutated_list[i]=random_alel[0]
    return to_be_mutated_list


def divide_list_into_sections(my_list, num_sections):
    section_size = len(my_list) // num_sections
    divided_sections = [my_list[n * section_size: (n + 1) * section_size] for n in range(num_sections)]
    return divided_sections


def mutation(parent_list, top_num_parents, child_return_num):
    # Sort parents based on fitness in descending order
    sorted_parents = sorted(parent_list, key=lambda x: x['fitness'], reverse=True)
    top_parents = []
    total_sub_list = []
    # gene_divider_num = len(parent_list[0]['genes']) / (child_return_num / top_num_parents)
    gene_divider_num = 30
    # loop through parent number sorting them
    for parent in range(0, top_num_parents):
        # sorted_parents[parent]['fitness']
        top_parents.append(sorted_parents[parent])

    # getting total sub list of top parents from ordered list of top parents
    for parent_list in top_parents:
        sub_list = divide_list_into_sections(parent_list['genes'], int(gene_divider_num))
        # print('sub list', sub_list)
        total_sub_list.append(sub_list)

    print('total_sub_list', total_sub_list)
    combined_lists = list(zip(*total_sub_list))

    # print("ba", combined_lists)
    # print('top parents', top_parents)
    # print(gene_divider_num)
    new_gen = []
    for instance in range(0, int(child_return_num/top_num_parents)):
        after_list = []
        # Print the grouped lists
        for group in combined_lists:
            fixed_list = list(group)
            # print("Grouped elements before:", fixed_list)
            random.shuffle(fixed_list)
            # print("Grouped elements after:", fixed_list)
            after_list.append(fixed_list)
        # print(after_list)

        final_list = []
        for k in after_list:
            for l in range(0, 2):
                final_list.append(k[l])

        # print(len(final_list))

        # Separate 0s and 1s dynamically
        separated_lists = [[] for _ in range(top_num_parents)]
        for i, element in enumerate(final_list):
            separated_lists[i % top_num_parents].append(element)

        # Print the separated lists
        for i, separated_list in enumerate(separated_lists):
            # print(f"{i}s list:", separated_list)
            flattened_list = [item for sublist in separated_list for item in sublist]
            # print("Flattened list:", flattened_list)
            new_gen.append(flattened_list)

    # new_gen = sorted(new_gen, key=lambda x: sum(x), reverse=False)
    # print("new gen", len(new_gen))
    for gen in range(0, int(len(new_gen)/2)):
        new_gen[gen] = mutate_list(new_gen[gen])

    new_gen_children_list = []
    for new_gen_child in new_gen:
        fitness_rank_child = fitness_fun(new_gen_child, version_try)
        child_dict = {'genes': new_gen_child, 'fitness': fitness_rank_child}
        new_gen_children_list.append(child_dict)
    return new_gen_children_list


def random_binary_list(length):
    return [random.choice([0, 1]) for _ in range(length)]


comp1 = random_binary_list(30)


def fitness_fun(child_list, version=1.1):
    # 1,1,1,0,1,0,1
    length_of_child_list = len(child_list)

    score = 0
    if version == 1.1:
        fitness_score = sum(child_list)
        return fitness_score

    if version == 1.2:
        for i in range(0, len(comp1)):
            if comp1[i] == child_list[i]:
                score = score + 1
        return score
    if version == 1.3:
        if sum(child_list) == 0:
            return len(children_list)*2
        else:
            fitness_score = sum(child_list)
            return fitness_score


def max_score(gen_dict):
    max_fitness_child = max(gen_dict, key=lambda x: x['fitness'])['fitness']
    return max_fitness_child


for i in range(10):
    length_of_list = 30
    random_list = random_binary_list(length_of_list)
    fitness_rank = fitness_fun(random_list, version_try)
    child_dict = {'genes': random_list, 'fitness': fitness_rank}
    children_list.append(child_dict)

print(len(children_list))
print("children list", children_list)
max_and_average_scores(children_list)
children_per_gen = 60

gen1 = mutation(children_list, 2, children_per_gen)
max_and_average_scores(gen1)
gen2 = mutation(gen1, 2, children_per_gen)
max_and_average_scores(gen2)
gen3 = mutation(gen2, 2, children_per_gen)
max_and_average_scores(gen3)
gen4 = mutation(gen3, 2, children_per_gen)
max_and_average_scores(gen4)
gen5 = mutation(gen4, 2, children_per_gen)
max_and_average_scores(gen5)


ypoints = np.array([max_score(children_list), max_score(gen1), max_score(gen2), max_score(gen3), max_score(gen4), max_score(gen5)])

plt.plot(ypoints, marker='o')
plt.show()
