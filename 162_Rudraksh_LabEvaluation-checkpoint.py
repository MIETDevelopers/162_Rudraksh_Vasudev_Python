{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7165e8da",
   "metadata": {},
   "source": [
    "# Rudraksh_2020A1R162\n",
    "\n",
    "#Implement Employee Management System\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "75a4b3e8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3530284116.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [2]\u001b[1;36m\u001b[0m\n\u001b[1;33m    def employee:\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d41bcd59",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'mysql'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Input \u001b[1;32mIn [3]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmysql\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mconnector\u001b[39;00m\n\u001b[0;32m      4\u001b[0m con \u001b[38;5;241m=\u001b[39m mysql\u001b[38;5;241m.\u001b[39mconnector\u001b[38;5;241m.\u001b[39mconnect(\n\u001b[0;32m      5\u001b[0m \thost\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlocalhost\u001b[39m\u001b[38;5;124m\"\u001b[39m, user\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mroot\u001b[39m\u001b[38;5;124m\"\u001b[39m, password\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpassword\u001b[39m\u001b[38;5;124m\"\u001b[39m, database\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124memp\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m# Function To Check if Employee with\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;66;03m# given Id Exist or Not\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'mysql'"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4b13bb57",
   "metadata": {},
   "outputs": [],
   "source": [
    "main_list = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7ae660bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of Employee to be added: 2\n",
      "\n",
      "Enter the NAME of the employee: ABC\n",
      "Enter the ID of the employee: 1111\n",
      "Enter the DEPARTMENT of the employee: CSE\n",
      "Enter the SALARY of the employee: 1000000\n",
      "\n",
      "Enter the NAME of the employee: DEF\n",
      "Enter the ID of the employee: 2222\n",
      "Enter the DEPARTMENT of the employee: ECE\n",
      "Enter the SALARY of the employee: 120202\n",
      "\n"
     ]
    }
   ],
   "source": [
    "count = int(input('Enter the number of Employee to be added: '))\n",
    "print('')\n",
    "for i in range(count):\n",
    "    sublist = ()\n",
    "    name = input('Enter the NAME of the employee: ')\n",
    "    emp_id = input('Enter the ID of the employee: ')\n",
    "    department = input('Enter the DEPARTMENT of the employee: ')\n",
    "    salary = int(input('Enter the SALARY of the employee: '))\n",
    "    print('')\n",
    "    sublist+=(name,emp_id,department,salary)\n",
    "    main_list.append(sublist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1a36f2e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('ABC', '1111', 'CSE', 1000000), ('DEF', '2222', 'ECE', 120202)]\n"
     ]
    }
   ],
   "source": [
    "print(main_list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "363beb0d",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
