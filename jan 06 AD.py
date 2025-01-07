{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "30c3b9ba-8151-4a8e-b46c-f7d135d43caf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original list: [1, 'hello', 3.14, True]\n",
      "List after appending 'World': [1, 'hello', 3.14, True, 'world']\n"
     ]
    }
   ],
   "source": [
    "my_list = [1, 'hello', 3.14, True]\n",
    "print(\"Original list:\", my_list)\n",
    "my_list.append('world')\n",
    "print(\"List after appending 'World':\", my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a6ce24f1-e75c-42f0-85d2-5e6d9b30e857",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List after removing 3.14: [1, 'hello', True, 'world']\n"
     ]
    }
   ],
   "source": [
    "my_list.remove(3.14)\n",
    "print(\"List after removing 3.14:\", my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "33230cf1-fcca-4445-8d5b-df4cb39f8d6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original tuple: [1, 'hello', 3.14, True]\n",
      "First element: 1\n",
      "Last element: True\n"
     ]
    }
   ],
   "source": [
    "my_tuple = [1, 'hello', 3.14, True]\n",
    "print(\"Original tuple:\", my_tuple)\n",
    "print(\"First element:\", my_tuple[0])\n",
    "print(\"Last element:\", my_tuple[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "918a94b9-de14-44d9-9b00-071adad3b293",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 6):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a3eb1b2b-0234-4f6c-8930-30e877beed7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "i = 1\n",
    "while i <= 5:\n",
    "    print(i)\n",
    "    i += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "76491146-bca4-42df-adaa-e530f56743c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  1\n",
      "Enter a number:  -1\n",
      "Enter a number:  2\n",
      "Enter a number:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number1 is Positive.\n",
      "The number2 is Negative.\n",
      "The number3 is Positive.\n",
      "The number4 is Zero.\n"
     ]
    }
   ],
   "source": [
    "number1 = int(input(\"Enter a number: \"))\n",
    "number2 = int(input(\"Enter a number: \"))\n",
    "number3 = int(input(\"Enter a number: \"))\n",
    "number4 = int(input(\"Enter a number: \"))\n",
    "if number1 > 0:\n",
    "    print(\"The number1 is Positive.\")\n",
    "elif number1 < 0:\n",
    "    print(\"The number1 is Negative.\")\n",
    "else:\n",
    "    print(\"The number1 is Zero.\")\n",
    "if number2 > 0:\n",
    "    print(\"The number2 is Positive.\")\n",
    "elif number2 < 0:\n",
    "    print(\"The number2 is Negative.\")\n",
    "else:\n",
    "    print(\"The number2 is Zero.\")\n",
    "if number3 > 0:\n",
    "    print(\"The number3 is Positive.\")\n",
    "elif number3 < 0:\n",
    "    print(\"The number3 is Negative.\")\n",
    "else:\n",
    "    print(\"The number3 is Zero.\")\n",
    "if number4 > 0:\n",
    "    print(\"The number4 is Positive.\")\n",
    "elif number4 < 0:\n",
    "    print(\"The number4 is Negative.\")\n",
    "else:\n",
    "    print(\"The number4 is Zero.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "03f633b9-2d09-4d5e-9ab5-44dd1c32e97e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello from Kamalesh, Saiteja!\n"
     ]
    }
   ],
   "source": [
    "def greet(Kamalesh):\n",
    "    print(f\"Hello from Kamalesh, {Kamalesh}!\")\n",
    "greet(\"Saiteja\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "372e5548-d25b-4e4c-a679-c6a3d43e757a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']\n"
     ]
    }
   ],
   "source": [
    "print(dir(str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "743f77e3-c67c-4c2f-b855-541d8b0324c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HI\n"
     ]
    }
   ],
   "source": [
    "a=\"hi\"\n",
    "b=a.upper()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "400bf482-96b9-4d3c-881c-cfb5b3bb2d3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi\n"
     ]
    }
   ],
   "source": [
    "a=\"HI\"\n",
    "b=a.lower()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f358b6de-6197-4a91-9ca6-b1afa661e571",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HI\n"
     ]
    }
   ],
   "source": [
    "a=\"hi\"\n",
    "b = a.swapcase()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a0b34207-a2af-4f31-ab30-f5289ad6153e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi kamalesh\n"
     ]
    }
   ],
   "source": [
    "a=\"hi hello\"\n",
    "b = a.replace('hello', 'kamalesh')\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "77681260-ec90-41f7-a212-46e13fc52112",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a=\"hi\"\n",
    "b = a.isdigit()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fd17c79c-44da-4260-afd0-ab058788f008",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=\"hi\"\n",
    "b = a.islower()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e03a4b1a-834e-40e1-9947-287a0d865b2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a=\"hi\"\n",
    "b = a.isupper()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1d7744b9-5bbf-44a6-9230-e0c49f7a32ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1]\n"
     ]
    }
   ],
   "source": [
    "a=range(2)\n",
    "b=list(a)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d04d076b-0283-4e36-b730-9b1c3d6d1a92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "264355\n"
     ]
    }
   ],
   "source": [
    "def add_numbers (a,b):\n",
    "    result = a+b\n",
    "    return result\n",
    "print(add_numbers(1999,262356))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cd4eb665-4aa3-4913-9d34-1d55741d164a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def greet(name, greeting=\"hello\"):\n",
    "    print(f\"{greeting}, {name}!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a478c83f-e8c0-4e69-b10a-fa163a8a9539",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum 0f 1,2,3,4: 10\n",
      "sum 0f 1,2,3: 6\n"
     ]
    }
   ],
   "source": [
    "def calculate_sum(*args):\n",
    "    total=sum(args)\n",
    "    return total\n",
    "print(\"sum 0f 1,2,3,4:\", calculate_sum(1,2,3,4))\n",
    "print(\"sum 0f 1,2,3:\", calculate_sum(1,2,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "59eb1f15-4e5a-4a6e-a86a-72133de206c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your username:  hfu\n",
      "Enter your password:  ewfu\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid username or password. please try again\n"
     ]
    }
   ],
   "source": [
    "a='hi'\n",
    "b='hello'\n",
    "c=input(\"Enter your username: \")\n",
    "d=input(\"Enter your password: \")\n",
    "if c==a and d==b:\n",
    "    print(\"login successful\")\n",
    "else:\n",
    "    print(\"invalid username or password. please try again\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "980fd613-b032-4514-917b-6bb370cd3a38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter an integer:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number 3 is Odd.\n"
     ]
    }
   ],
   "source": [
    "def check_even_odd(number):\n",
    "    if number % 2 == 0:\n",
    "        return \"Even\"\n",
    "    else:\n",
    "        return \"Odd\"\n",
    "num = int(input(\"Enter an integer: \"))\n",
    "result = check_even_odd(num)\n",
    "print(f\"The number {num} is {result}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ef6ea064-fde1-46b4-9e0c-b5ba561fe8f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original List: [-10, 25.5, -3.7, 42, 0]\n",
      "Absolute Values: [10, 25.5, 3.7, 42, 0]\n",
      "Rounded Values: [-10, 26, -4, 42, 0]\n",
      "Data Type of 'numbers': <class 'list'>\n",
      "Sorted List: [-10, -3.7, 0, 25.5, 42]\n"
     ]
    }
   ],
   "source": [
    "numbers=[-10, 25.5, -3.7, 42, 0]\n",
    "absolute_values=[abs(num) for num in numbers]\n",
    "rounded_values=[round(num) for num in numbers]  \n",
    "data_type=type(numbers) \n",
    "sorted_numbers=sorted(numbers)  \n",
    "print(\"Original List:\", numbers)\n",
    "print(\"Absolute Values:\", absolute_values)\n",
    "print(\"Rounded Values:\", rounded_values)\n",
    "print(\"Data Type of 'numbers':\", data_type)\n",
    "print(\"Sorted List:\", sorted_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9e31611c-d6c3-47b2-a7d9-431a229cbc77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the radius of the circle:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of the circle with radius 3.0 is 28.27\n"
     ]
    }
   ],
   "source": [
    "def calculate_circle_area(radius):\n",
    "    pi = 3.14159\n",
    "    area = pi * radius ** 2\n",
    "    return area\n",
    "radius = float(input(\"Enter the radius of the circle: \"))\n",
    "area = calculate_circle_area(radius)\n",
    "print(f\"The area of the circle with radius {radius} is {area:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0ea02b04-d13d-463c-b9b7-381c357cffc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the radius of the circle:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of the circle with radius 3.0 is 28.27\n"
     ]
    }
   ],
   "source": [
    "def calculate_circle_area(radius):\n",
    "    pi = 3.14159\n",
    "    area = pi * radius ** 2\n",
    "    return area\n",
    "radius = float(input(\"Enter the radius of the circle: \"))\n",
    "area = calculate_circle_area(radius)\n",
    "print(f\"The area of the circle with radius {radius} is {area:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9ad1fb65-c26a-4915-8433-2eef9735ee45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the radius of the circle:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of the circle with radius 3.0 is 28.27\n"
     ]
    }
   ],
   "source": [
    "def calculate_circle_area(radius):\n",
    "    pi = 3.14159\n",
    "    area = pi * radius ** 2\n",
    "    return area\n",
    "radius = float(input(\"Enter the radius of the circle: \"))\n",
    "area = calculate_circle_area(radius)\n",
    "print(f\"The area of the circle with radius {radius} is {area:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e095b70a-7982-4c60-9698-b53d86e77dfd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the radius of the circle:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of the circle with radius 3.0 is 28.27\n"
     ]
    }
   ],
   "source": [
    "def calculate_circle_area(radius):\n",
    "    pi = 3.14159\n",
    "    area = pi * radius ** 2\n",
    "    return area\n",
    "radius = float(input(\"Enter the radius of the circle: \"))\n",
    "area = calculate_circle_area(radius)\n",
    "print(f\"The area of the circle with radius {radius} is {area:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7834b5c6-682d-4434-a49e-0e1a8934f4c8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
