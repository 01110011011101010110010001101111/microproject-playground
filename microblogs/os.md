# Operating Systems!

## Intro to Pagetables: Concept

Memory. Something that seems like it might be somewhat trivial is actually a pretty involved mechanism for OSes. Recall that an OS wants each of its processes to seem like it's by itself, which means it wants to seem like it has its own memory. In addition, recall that an OS cares about security: it doesn't want one process able to tamper with the memory of another. 

How exactly could you get the OS to give each process its own memory and make sure different processes don't mess with each other's memory? Insert the idea of pagetables. In this sense, there are two types of memory: virtual memory (which the CPU can interact with) and physical memory (the actual DRAM). A pagetable is a mechanism that can be used to map the virtual memory to physical memory. Giving each process its own page table gives each process its own chunk of memory all for itself. Furthermore, the only physical memory it can map to depends on the pagetable—this can prevent a process from writing all over random physical memory.

