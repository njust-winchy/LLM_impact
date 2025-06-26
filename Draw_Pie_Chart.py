import matplotlib.pyplot as plt

# Data
categories = ['Summary', 'Motivation', 'Substance', 'Replicability', 'Originality', 'Soundness', 'Clarity', 'Meaningful Comparison']
#ICLR_ai_values = [21981, 4516, 5721, 808, 4129, 5958, 4706, 1758]
#NIPS_ai_values = [12587, 3172, 3648, 492, 2437, 4110, 3069, 1052]
ICLR_no_ai = [80346, 20433, 24303, 11330, 33848, 35578, 43630, 11341]
#NIPS_no_ai = [46013, 8445, 9917, 2158, 9293, 14540, 14168, 4546]
# Calculate percentage
total = sum(ICLR_no_ai)
percentages = [(v / total) * 100 for v in ICLR_no_ai]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
plt.title('The distribution of aspect focus in no AI-assisted review reports in ICLR.')

# Show the plot
plt.savefig('iclr_no_ai.png')
plt.show()
