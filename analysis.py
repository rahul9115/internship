{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import pylab as pl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date (dd/mm/yyyy)</th>\n",
       "      <th>Startup Name</th>\n",
       "      <th>Amount (In USD)</th>\n",
       "      <th>Industry / Vertical</th>\n",
       "      <th>Sub-Vertical</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>09-04-2020</td>\n",
       "      <td>Vedantu</td>\n",
       "      <td>1,25,60,000</td>\n",
       "      <td>EduTech</td>\n",
       "      <td>Online Tutoring</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Date (dd/mm/yyyy) Startup Name Amount (In USD) Industry / Vertical  \\\n",
       "95        09-04-2020      Vedantu     1,25,60,000             EduTech   \n",
       "\n",
       "       Sub-Vertical  \n",
       "95  Online Tutoring  "
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv('merge.csv')\n",
    "cdf1=df.loc[df['Startup Name']=='Vedantu']\n",
    "cdf1[['Date (dd/mm/yyyy)','Startup Name','Amount (In USD)','Industry / Vertical','Sub-Vertical']]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date dd/mm/yyyy</th>\n",
       "      <th>Startup Name</th>\n",
       "      <th>Amount in USD</th>\n",
       "      <th>Industry Vertical</th>\n",
       "      <th>SubVertical</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>286</th>\n",
       "      <td>05/04/2018</td>\n",
       "      <td>Vedantu</td>\n",
       "      <td>1,00,00,000</td>\n",
       "      <td>Ed-Tech</td>\n",
       "      <td>Interactive Online Tutoring Platform</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2767</th>\n",
       "      <td>07/05/2015</td>\n",
       "      <td>Vedantu</td>\n",
       "      <td>50,00,000</td>\n",
       "      <td>Online Education Platform</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date dd/mm/yyyy Startup Name Amount in USD          Industry Vertical  \\\n",
       "286       05/04/2018      Vedantu   1,00,00,000                    Ed-Tech   \n",
       "2767      07/05/2015      Vedantu     50,00,000  Online Education Platform   \n",
       "\n",
       "                               SubVertical  \n",
       "286   Interactive Online Tutoring Platform  \n",
       "2767                                   NaN  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv('startup_funding (1).csv')\n",
    "cdf=df.loc[df['Startup Name']=='Vedantu']\n",
    "cdf[['Date dd/mm/yyyy','Startup Name','Amount in USD','Industry Vertical','SubVertical']]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10000000.0\n",
      "5000000.0\n",
      "yo [5000000.0, 10000000.0]\n",
      "12560000.0\n",
      "[5000000.0, 10000000.0, 12560000.0]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x1=cdf1['Date (dd/mm/yyyy)'].values\n",
    "y1=cdf1['Amount (In USD)'].values\n",
    "x=cdf['Date dd/mm/yyyy'].values\n",
    "y=cdf['Amount in USD'].values\n",
    "amount=''\n",
    "z=[]\n",
    "x2=[]\n",
    "for i in y:\n",
    "    for j in i:\n",
    "        if j==\",\":\n",
    "            continue\n",
    "        else:\n",
    "            amount=amount+j\n",
    "    i=float(amount)\n",
    "    print(i)\n",
    "    z.append(i)\n",
    "    amount=''\n",
    "z.reverse()\n",
    "print(\"yo\",z)\n",
    "for i in y1:\n",
    "    for j in i:\n",
    "        if j==\",\":\n",
    "            continue\n",
    "        else:\n",
    "            amount=amount+j\n",
    "    i=float(amount)\n",
    "    print(i)\n",
    "    z.append(i)\n",
    "    amount=''\n",
    "for i in x:\n",
    "    x2.append(i)\n",
    "x2.reverse()\n",
    "for i in x1:\n",
    "    x2.append(i)\n",
    "print(z)    \n",
    "plt.plot(x2,z,color=\"blue\")\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Vedantuc Funds')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['05/04/2018' '07/05/2015']\n"
     ]
    }
   ],
   "source": [
    "x=cdf['Date dd/mm/yyyy'].values\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
