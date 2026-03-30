import numpy as np
import matplotlib.pyplot as plt


def define_piecewise_function():
    """Определяет кусочно-заданную функцию с использованием np.piecewise."""
    def first_piece(x):
        return np.cos(x + x**3)

    def second_piece(x):
        return np.exp(-x**2) - x**2 + 2 * x

    def f(x):
        conditions = [(x >= 0) & (x <= 1), (x > 1) & (x <= 2)]
        return np.piecewise(x, conditions, [first_piece, second_piece])

    return f


def define_derivative():
    """Определяет производную функции для каждого куска."""
    def der_first(x):
        return -np.sin(x + x**3) * (1 + 3 * x**2)

    def der_second(x):
        return -2 * x * np.exp(-x**2) - 2 * x + 2

    def f_prime(x):
        return np.where((x >= 0) & (x <= 1), der_first(x), der_second(x))

    return f_prime


def calculate_tangent_params(x0, f, f_prime):
    """Вычисляет параметры касательной в точке x0."""
    y0 = f(x0)
    slope = f_prime(x0)
    return y0, slope


def generate_plot_data(f, x0, y0, slope):
    """Генерирует данные для графика функции и касательной."""
    x = np.linspace(0, 2, 2000)
    y = f(x)

    # Ограничиваем касательную первым куском для аккуратности
    x_tan = np.linspace(0, 1.0, 600)
    y_tan = y0 + slope * (x_tan - x0)

    return x, y, x_tan, y_tan


def print_tangent_info(x0, y0, slope):
    """Выводит информацию о точке касания в консоль."""
    print(f"Точка касания: x = {x0}")
    print(f"f({x0})  = {y0:.6f}")
    print(f"f'({x0}) = {slope:.6f}")


def create_and_configure_plot(x, y, x_tan, y_tan, x0, y0, slope):
    """Создаёт и настраивает график с использованием matplotlib."""
    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(x, y, color='blue', linewidth=2.0, label='f(x) — кусочная функция')
    ax.plot(x_tan, y_tan, color='red', linestyle='--', linewidth=2.0,
            label=f'Касательная в точке x = {x0}')
    ax.scatter([x0], [y0], color='red', s=100, zorder=5, label='Точка касания')

    # Аннотация с синтаксическим сахаром форматированных строк
    ax.annotate(
        f'Касание в x = {x0}\n'
        f'f({x0}) ≈ {y0:.4f}\n'
        f"f'({x0}) ≈ {slope:.4f}",
        xy=(x0, y0),
        xytext=(x0 + 0.45, y0 + 1.0),
        arrowprops=dict(facecolor='black', shrink=0.05, width=1.0),
        bbox=dict(boxstyle="round,pad=0.7", facecolor="yellow", alpha=0.95),
        fontsize=12
    )

    ax.set_title('График кусочно-заданной функции и касательной к ней',
                 fontsize=17, fontweight='bold', pad=25)
    ax.set_xlabel('x', fontsize=14)             # Ось абсцисс
    ax.set_ylabel('f(x)', fontsize=14)          # Ось ординат
    ax.grid(True, linestyle='--', alpha=0.9)    # Включение отображение сетки
    ax.legend(fontsize=13, loc='upper right')   # Размещение легенды на графике

    # Линия разрыва
    ax.axvline(x=1, color='gray', linestyle=':', alpha=0.8, linewidth=1.5)

    ax.set_xlim(0, 2)
    ax.set_ylim(-1, 3)

    plt.tight_layout()
    plt.show()


def main():
    """Основная функция для запуска скрипта."""
    f = define_piecewise_function()
    f_prime = define_derivative()

    x0 = 0.5
    y0, slope = calculate_tangent_params(x0, f, f_prime)

    print_tangent_info(x0, y0, slope)

    x, y, x_tan, y_tan = generate_plot_data(f, x0, y0, slope)

    create_and_configure_plot(x, y, x_tan, y_tan, x0, y0, slope)


if __name__ == "__main__":
    main()