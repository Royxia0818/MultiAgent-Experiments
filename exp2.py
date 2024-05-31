def greedy_resource_allocation(agents, resources):
    # 按照每个任务所需资源从小到大排序
    agents.sort(key=lambda x: x[2]/x[1])
    work = 0
    allocated_tasks = []
    for agent in agents:
        task_id, required_resource, job_done = agent
        if resources >= required_resource:
            allocated_tasks.append(agent)
            resources -= required_resource
            work += job_done

    return allocated_tasks, resources, work

# 示例任务和资源
agents = [
    (1, 2, 6),  # agent1需要2个资源，能完成6份工作
    (2, 1, 2),  # agent2需要1个资源，能完成2份工作
    (3, 4, 9),  # agent3需要4个资源，能完成9份工作
    (4, 3, 7),  # agent4需要3个资源，能完成7份工作
    (5, 2, 5)   # agent5需要2个资源，能完成5份工作
]
total_resources = 9  # 总资源数量

# 调用贪心资源分配函数
allocated_agents, remaining_resources, work = greedy_resource_allocation(agents, total_resources)

# 打印分配结果
print("Allocated agents:", allocated_agents)
print("Remaining resources:", remaining_resources)
print(f"Work complete: {work}")
