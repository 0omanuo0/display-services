export async function fetchData() {

    try {
        const response = await fetch('http://127.0.0.1:5000/status');
        const data = await response.json();

        const cpu = data.node.cpu;
        const memory = data.node.memory.used;
        const maxmemory = data.node.memory.total;

        const containers = data.containers;

        const VM = data.vm;
        
        const services = data.services;

        return { cpu, memory, maxmemory, containers, VM, services };
        
    } catch (error) {
        console.error(error);

        return { cpu: NaN, memory: NaN, maxmemory: NaN, containers: [], VM: [] };
    }
}