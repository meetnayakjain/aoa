def job_sequencing_with_deadline(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]

    time_slots = [0] * max_deadline

    selected_jobs = []

    for job in jobs:

        deadline = job[1]

        for i in range(deadline - 1, -1, -1):

            if time_slots[i] == 0:

                time_slots[i] = job[0]

                selected_jobs.append(job)

                break

    total_profit = sum(job[2] for job in selected_jobs)

    return total_profit, selected_jobs

jobs = []

n = int(input("Enter the number of jobs: "))

for i in range(n):

    job_id = input("Enter job ID: ")

    deadline = int(input("Enter deadline for job {}: ".format(job_id)))

    profit = int(input("Enter profit for job {}: ".format(job_id)))

    jobs.append((job_id, deadline, profit))

max_profit, selected_jobs = job_sequencing_with_deadline(jobs)

print("Maximum profit:", max_profit)

print("Selected jobs:", [job[0] for job in selected_jobs])
