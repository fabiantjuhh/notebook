<script>
	export let data;

	let rows = data.data || [];
	let columns = rows.length > 0 ? Object.keys(rows[0]) : [];
	console.log(rows);
</script>

<h1 class="text-center text-2xl font-bold">Test Table</h1>

<div class="mt-10 flex justify-center">
	<figure>
		<table class="table-auto border border-gray-300 text-center w-full">
			<thead class="bg-gray-100">
				<tr>
					{#each columns as col}
						<th class="border border-gray-300 px-4 py-2">{col}</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#each data.data as row}
					<tr>
						{#each columns as col}
							<td class="border border-gray-300 px-4 py-2">{row[col]}</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
		<figcaption class="mt-2 text-center text-sm text-gray-500">
			Data fetched from FastAPI, displayed in a table format. Using Svelte for reactivity and
			Tailwind CSS for styling and Python for backend.
		</figcaption>
	</figure>
</div>
