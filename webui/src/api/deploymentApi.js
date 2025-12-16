export async function fetchTodayDeployments() {
  const res = await fetch("/api/deployments/today");

  if (!res.ok) {
    throw new Error("Failed to fetch deployments");
  }

  return res.json();
}
