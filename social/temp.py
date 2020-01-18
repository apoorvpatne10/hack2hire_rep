import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "apoorvwatsky@gmail.com"
password = 'Testing@999'
receiver_email = "apoorv.patne10@gmail.com"
message = "Hey there! Python testing now!"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

#
#
# get_rule = Rule.objects.get(pk=1)
# all_names = User.objects.order_by().values('name').distinct()
#
# for i, na in enumerate(all_names):
#     current_user = User.objects.filter(name=na['name'])
#     di_user = defaultdict(float)
#     score = 0
#
#     for obj in current_user:
#         di_user[obj.item] += obj.value
#
#     for x, y in di_user.items():
#         if x == 'Traffic Challan':
#             if y >= get_rule.traffic_challan_value:
#                 score = score + y*get_rule.traffic_challan_weight
#             else:
#                 score = score + y*(-get_rule.traffic_challan_weight)
#         elif x == 'Penalty Taxes':
#             if y >= get_rule.penalty_tax_value:
#                 score = score + y*get_rule.penalty_tax_weight
#             else:
#                 score = score + y*(-get_rule.penalty_tax_weight)
#         elif x == 'Utility Bills':
#             if y >= get_rule.utility_bills_value:
#                 score = score + y*get_rule.utility_bills_weight
#             else:
#                 score = score + y*(-get_rule.utility_bills_weight)
#         elif x == 'Charges Electric Car':
#             if y >= get_rule.charges_electric_value:
#                 score = score + y*get_rule.charges_electric_weight
#             else:
#                 score = score + y*(-get_rule.charges_electric_weight)
#
#     if score >= get_rule.threshold_value:
#         approved = True
#     else:
#         approved = False
#
#     my_user = MyUser.objects.create(uid=i, uname=na['name'], score=score, approved=approved)
#     my_user.save()
