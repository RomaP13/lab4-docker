# Модель: Метод Ньютона (5 семестр)
# Автор: Помазан Роман, група АІ-233


def f(x: int) -> float:
    """Функція: x^3 - 2x^2 - 5x + 6 = 0"""
    return x**3 - 2 * x**2 - 5 * x + 6


def df(x: int) -> float:
    """Похідна функції"""
    return 3 * x**2 - 4 * x - 5


def newton_method(x0: float, tol: float = 1e-4, max_iter: int = 50) -> int | float:
    """Метод Ньютона"""
    x = x0
    print(f"Початкове наближення: x0 = {x0}")

    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            print(f"\nКорінь знайдено за {i} ітерацій: x ≈ {x:.6f}")
            return x

        x_new = x - fx / df(x)
        print(f"Ітерація {i + 1:2d}: x = {x_new:.6f}, f(x) = {fx:.6f}")
        x = x_new

    print("Досягнуто максимальну кількість ітерацій.")
    return x


if __name__ == "__main__":
    print(
        "=== Розв'язання нелінійного рівняння x³ - 2x² - 5x + 6 = 0 методом Ньютона ===\n"
    )

    import os

    mode = os.getenv("MODE", "eco")
    print(f"Режим роботи: {mode.upper()}\n")

    # Початкові наближення
    roots = []
    for x0 in [-2.0, 1.0, 3.0]:
        print(f"\n--- Початкове наближення x0 = {x0} ---")
        root = newton_method(x0)
        roots.append(root)

    print("\nЗнайдені корені:", [round(r, 6) for r in roots])
