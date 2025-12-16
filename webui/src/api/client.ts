export async function api(
  url: string,
  token?: string,
  options: RequestInit = {}
) {
  const res = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });

  // 🔴 AUTO LOGOUT WHEN JWT EXPIRED
  if (res.status === 401) {
    localStorage.removeItem("auth");
    window.location.reload(); // quay về Login
    throw new Error("Unauthorized");
  }

  if (!res.ok) {
    throw new Error(await res.text());
  }

  return res.json();
}
