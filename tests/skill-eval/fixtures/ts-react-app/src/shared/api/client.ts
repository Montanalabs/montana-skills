export async function getJson(path: string) {
  const response = await fetch(path);
  return response.json();
}
