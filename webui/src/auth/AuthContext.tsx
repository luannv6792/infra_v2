import { createContext, useContext, useState } from "react";

type User = { token: string; role: "admin" | "developer" } | null;

const AuthContext = createContext({
  user: null as User,
  login: (u: User) => {},
  logout: () => {},
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User>(() => {
    const raw = localStorage.getItem("auth");
    return raw ? JSON.parse(raw) : null;
  });

  const login = (u: User) => {
    setUser(u);
    localStorage.setItem("auth", JSON.stringify(u));
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("auth");
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
