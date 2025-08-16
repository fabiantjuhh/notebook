export async function load({ fetch }) {
    const res = await fetch('http://127.0.0.1:8000/data');
    const data = await res.json();

    return {
        data
    };
}