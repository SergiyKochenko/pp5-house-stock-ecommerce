# Portfolio Project 5 - Home Store & More eCommerce Webstore

This repository contains the source code for the Home Store & More eCommerce webstore, a full stack web application developed as a portfolio project for The Code Institute's Full Stack Software Development (eCommerce) Diploma program. The website can be viewed at <https://pp5-house-stock-ecommerce.herokuapp.com/>.

# Overview

Welcome to [Home Store & More](https://pp5-house-stock-ecommerce.herokuapp.com/)
This Website is an e-Commerce Webstore that was designed and developed as an Portfolio Project for The Code Institute's Full Stack Software Development (eCommerce) Diploma programme.

Home Store & More is a demo e-commerce platform showcasing a wide range of affordable, full-stock home products and solutions catering to a diverse and growing target audience. The project demonstrates the developer's proficiency in creating a comprehensive e-commerce solution, with an appealing design, intuitive navigation, and responsive layout.

Please note that this project is for assessment purposes only and does not accept real credit or debit card payments. Any purchases or bookings made on the website will not be fulfilled.

The project is for assessment purposes only and will not accept any genuine credit or debit card payments and any purchases or booking made will not be fullfilled. The [Home Store & More](https://pp5-house-stock-ecommerce.herokuapp.com/) is a full stack, E-commerce, web application offering affordable, full ctock home products and solutions to a growing and diverse target audience.

- User Interface and Design: The website features a visually appealing and modern design, making it easy for users to browse and navigate the site. The layout is responsive, ensuring that the website looks great on various devices, including desktops, laptops, tablets, and smartphones.

- Product Catalog: Home Store & More offers a wide range of home products and solutions, organized into different categories for easy browsing. Users can explore various sections to find the items they're looking for, whether it's home decor, furniture, kitchenware, or other household essentials.
  
- Search Functionality: The website includes a search feature that allows users to quickly find specific products by entering relevant keywords or phrases. This function enhances the overall user experience and helps shoppers locate their desired items with ease.
  
- User Accounts and Authentication: Home Store & More has implemented user account creation and authentication, allowing users to create profiles, save their preferences, and view their order history. This feature demonstrates the developer's ability to integrate essential user management components in an e-commerce platform.
  
- Shopping Cart and Checkout: The website incorporates a shopping cart system that enables users to add products to their cart, review their selections, and proceed to the checkout process. Though it doesn't accept real credit or debit card payments, the website demonstrates the developer's understanding of integrating a seamless and secure checkout experience.
  
- Performance and Optimization: The Home Store & More website is built with performance in mind, ensuring fast load times and an optimized user experience. This aspect showcases the developer's knowledge of best practices in web development and their ability to create a high-performing e-commerce platform.

Overall, the Home Store & More website is a well-rounded e-commerce web application that demonstrates the developer's expertise in full stack web development, specifically in the context of e-commerce. The website is an excellent portfolio project that highlights their proficiency in various aspects of web development, from front-end design to back-end functionality, and provides a strong foundation for potential future projects.

Please use the link below to view the deployed project. If you wish to make a mock purchase, you can use the following details:

- Card Number: 4242424242424242
- Exp Date: Any (future) date using the format MM/YY
- CVN = any 3 digit number
- Postcode = any 5 numerals

Any payments made using an actual payment card will fail and the card will not be charged. No orders made will be fulfilled.

Live project: [Home Store & More](https://pp5-house-stock-ecommerce.herokuapp.com/) app.

The [GitHub repository](https://github.com/SergiyKochenko/pp5-house-stock-ecommerce)

[Back to the Table of Contents](#table-of-contents)

# Amiresponsive - "Home Store & More".

![](static/assets/images/amiresponsive.png)

## Table of contents

- [Overview](#overview)
  - [Project goals](#project-goals)
  - [Web Marketing Strategy](#web-marketing-strategy)
  - - [MailChimp](#mailchimp)
  - [UX (User Experience)](#ux-user-experience)
  - [User Experience](#user-experience)
  - [User stories](#user-stories)
  - [Site Administrator goals](#site-administrator-goals)
- [Design Structure](#design-structure)
  - [Color Scheme](#color-scheme)
  - [Functional Structure](#functional-structure)
  - - [404 page](#404-page)
  - - [403 page](#403-page)
  - - [500 page](#500-page)
  - [Wireframes](#wireframes)
  - - [For Desktop view](#for-desktop-view)
  - - [For Mobile view and small screens](#for-mobile-view-and-small-screens)
- [Features](#features)
  - [Navbar](#navbar)
  - [Home page](#home-page)
  - [Products page](#products-page)
  - [Product Detail page](#product-detail-page)
  - [Wishlist page](#wishlist-page)
  - [About page](#about-page)
  - [Testimonials page](#testimonials-page)
  - [Hire page](#hire-page)
  - [Packages page](#packages-page)
  - [Footer](#footer)
  - [Basket page](#basket-page)
  - [Checkout page](#checkout-page)
  - [Sign up page](#sign-up-page)
  - [Login page](#login-page)
  - [Responsive design](#responsive-design)
  - [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
- [Installed Packages](#installed-packages)
  - [Frameworks](#frameworks)
  - [Database](#database)
  - [Cloud Hosting](#cloud-hosting)
  - - [Additional Media Hosting](#additional-media-hosting)
  - [Tools](#tools)
- [Testing](#testing)
  - [Bugs](#bugs)
  - [Fixed Bugs](#fixed-bugs)
  - [Bug reports bug reports](#bug-reports-bug-reports)
  - [Unresolved Bugs](#unresolved-bugs)
- [Automated testing (Unit test)](#automated-testing-unit-test)
  - [Manual Testing](#manual-testing)
  - [Device Testing](#device-testing)
  - [Browsers Tested](#browsers-tested)
  - [Testing CRUD functionality](#testing-crud-functionality)
- [Validations](#validations)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Python Validation (PEP8)](#python-validation-pep8)
  - [Lighthouse report](#lighthouse-report)
- [Deployment](#deployment)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Contributing](#contributing)
  - [Inspiration](#inspiration)
  - [Acknowledgment](#acknowledgment)

## Project goals

The primary goals of the Home Store & More e-commerce webstore project are:

1. **Portfolio Showcase:** Demonstrate the developer's skills and capabilities in full-stack web development, specifically in the context of e-commerce, as part of The Code Institute's Full Stack Software Development (eCommerce) Diploma program.
   
2. **User Experience:** Create a visually appealing, responsive, and user-friendly web application that offers an intuitive browsing and shopping experience for a diverse and growing target audience.

3. **Product Catalog:** Design a comprehensive product catalog with a wide range of home products and solutions, organized into categories for easy browsing and navigation.
4. **Search and Filter:** Implement search functionality and filtering options, allowing users to quickly locate specific products and tailor their browsing experience according to their preferences.
   
5. **User Accounts and Authentication:** Integrate user account creation and authentication features, enabling users to create profiles, save their preferences, and view their order history.
   
6. **Shopping Cart and Checkout:** Develop a seamless shopping cart system and a simulated checkout process that demonstrates the understanding and implementation of a secure and user-friendly e-commerce transaction flow.
   
7. **Performance and Optimization:** Optimize the website for performance and fast load times, ensuring a smooth and enjoyable user experience.
   
8. **Scalability and Extensibility:** Build a solid foundation that allows for future expansion and refinement, making it possible to add new features, products, and functionalities as the platform grows.



## Web Marketing Strategy

The PP5 E-Commerce website aims to attract and convert visitors into customers by implementing a comprehensive web marketing strategy that focuses on the following key channels and tactics:

1. **Search Engine Optimization (SEO)**: Improve the website's organic search ranking by optimizing content, structure, and technical aspects for search engines.

2. **Content Marketing**: Create engaging and informative content, such as blog posts and articles, to attract potential customers and establish the website as an industry authority.

3. **Social Media Marketing**: Engage with users on popular social media platforms to promote content, share updates, and build brand awareness.

4. **Email Marketing**: Utilize email campaigns to keep subscribers informed about promotions, new products, and other updates.

5. **Influencer Marketing**: Partner with influencers in the home equipment and decor niche to reach a larger audience and boost brand visibility.

6. **Affiliate Marketing**: Encourage partners to promote the website and its products through an affiliate program.

7. **Conversion Rate Optimization (CRO)**: Continuously optimize the website's design, user experience, and calls-to-action to improve conversion rates.

By implementing this web marketing strategy, the PP5 House Stock E-Commerce website aims to increase online visibility, drive more traffic, and ultimately boost sales and revenue.

## MailChimp

### **MailChimp Integration for PP5 E-commerce:**

MailChimp is a powerful marketing platform that helps businesses manage their email marketing campaigns, subscriber lists, and automation workflows. 
<br>By integrating MailChimp with our PP5 E-commerce website, we can enhance user engagement, manage mailing lists, and keep customers 
<br>informed about new products, promotions, and important updates.

**Key Features**
1. **Email Marketing:** Easily create, send, and track personalized email campaigns to promote your products and services, ensuring that your customers stay informed and engaged.
2. **Subscriber Management:** Manage your subscribers' data, segment them based on their preferences, and create targeted campaigns for better conversion rates.
3. **Automation:** Set up automated workflows to send personalized and timely messages, such as welcome emails for new subscribers or abandoned cart reminders.
4. **Analytics and Reporting:** Track the performance of your email campaigns through detailed analytics, helping you make informed decisions to optimize your marketing efforts.
5. **Signup Forms:** Embed customizable signup forms on your website, enabling visitors to subscribe to your mailing list with ease.

**Integration Steps**
To integrate MailChimp with the PP5 E-commerce website, follow these steps:
1. Sign up for a MailChimp account or log in to your existing account.
2. Obtain your API key from the MailChimp dashboard.
3. In the PP5 House Stock E-commerce website's admin panel, navigate to the MailChimp integration settings.
4. Enter the API key in the designated field and save the settings.
5. Configure the integration settings, such as the audience list, email templates, and automation triggers.
6. Embed the MailChimp signup form on your website's front-end to enable users to subscribe to your mailing list.
7. Test the integration by sending a test email and verifying that it's correctly delivered to your subscribers.

**Support and Resources**
For more information about MailChimp and its features, visit the official MailChimp website (https://mailchimp.com/) and their knowledge base (https://mailchimp.com/help/).

**By integrating MailChimp with the PP5 E-commerce website, I can leverage the power of email marketing to build strong relationships with my customers and increase sales.**

[Back to the top](#table-of-contents)

## UX (User Experience)

### User Experience

UX, or User Experience, refers to the overall experience a user has while interacting with a product, service, or website. It encompasses various aspects of design, functionality, and usability to create a seamless and enjoyable experience for users. Here are some key elements to consider when creating a positive UX for the Home Store & More e-commerce webstore:

1. **Intuitive Navigation:** Design a clear and consistent navigation structure that allows users to easily move between different sections of the website. This can be achieved by using a well-organized menu with easy-to-understand labels and logical categorization of products and content.
   
2. **Responsive Design:** Ensure that the website looks and functions well on various devices and screen sizes, including desktops, laptops, tablets, and smartphones. This can be achieved by using responsive design techniques, such as fluid grids, flexible images, and media queries.
   
3. **Clear and Consistent Visual Hierarchy:** Establish a visual hierarchy that guides users through the content and makes it easy for them to understand the layout and organization of the website. Use consistent typography, color schemes, and design elements throughout the site to create a cohesive look and feel.

4. **Effective Search and Filtering:** Implement a search feature that allows users to quickly find specific products and content. Additionally, provide filtering options so users can refine their search results and browse products based on their preferences and requirements.
   
5. **Informative Product Pages:** Design detailed and informative product pages that provide users with all the necessary information to make informed purchase decisions. Include high-quality images, clear product descriptions, specifications, pricing, and customer reviews.
   
6. **User-friendly Forms:** Create simple and user-friendly forms for user registration, login, and checkout processes. Use clear labels, intuitive input fields, and helpful error messages to guide users through the process and minimize friction.
   
7. **Load Time Optimization:** Optimize the website's performance to ensure fast load times and a smooth user experience. This can be achieved by compressing images, minifying CSS and JavaScript files, and utilizing caching techniques.
   
8. **Accessibility:** Design the website with accessibility in mind, ensuring that users with disabilities can access and interact with the content. This can be achieved by using semantic HTML, proper color contrast, keyboard navigation support, and screen reader-friendly content.
   
By considering these aspects and focusing on creating a positive user experience, the Home Store & More e-commerce webstore will be more likely to engage users, encourage repeat visits, and ultimately drive conversions and sales

### User stories

See the GitHub Projects section was used as a [Kanban board](https://github.com/users/SergiyKochenko/projects/14) for the development of this project, which made it possible to break down the project execution into subtasks and make it easier to complete and track project progress.
[User stories](https://github.com/users/SergiyKochenko/projects/14) were used to break down the project into sub-tasks and placed on the Kanban board to work on them and track progress.

#### Site Administrator goals

Site Administrator Goals for the Home Store & More e-commerce webstore:

1. **Efficient Product Management:** Implement an easy-to-use and efficient product management system, allowing the site administrator to add, edit, and remove products, as well as manage product categories and inventory.
   
2. **Order Management:** Develop a comprehensive order management system that enables the site administrator to monitor and manage customer orders, track shipping statuses, and handle returns or refunds when necessary.
3. **User Management:** Implement a user management system that allows the site administrator to manage registered users, monitor user activity, and address any reported issues or concerns.
   
4. **Secure Payment Processing:** Ensure the secure handling and processing of payment information, even though the website currently does not accept real transactions, to demonstrate a commitment to security and data protection.

5. **Site Analytics and Reporting:** Integrate site analytics and reporting features that provide the site administrator with valuable insights into user behavior, popular products, sales trends, and other key performance indicators (KPIs).
   
6. **Marketing and Promotion:** Facilitate the creation and management of marketing campaigns and promotions, such as discounts, special offers, and email marketing, to drive traffic and increase sales.
   
7. **Content Management:** Implement an easy-to-use content management system (CMS) that allows the site administrator to update and maintain the website's content, including banners, blog posts, and static pages.

8. **Customer Support:** Develop a system for managing customer inquiries, complaints, and feedback, enabling the site administrator to provide timely and effective support to users.
   
9. **System Maintenance and Updates:** Ensure regular system maintenance and updates to keep the website running smoothly, address any potential security vulnerabilities, and implement new features and improvements as needed.

10. **Scalability and Performance:** Monitor and optimize the website's performance and infrastructure to ensure fast load times and a smooth user experience, as well as plan for scalability to accommodate future growth.

By focusing on these goals, the site administrator can effectively manage and maintain the Home Store & More e-commerce webstore, ensuring a positive experience for both users and the website's stakeholders.


[Back to the top](#table-of-contents)

## Design Structure

Design Structure for the Home Store & More e-commerce webstore:

1. Header: The header section should include the website's logo, a search bar, user account options (login, register, account settings), and a shopping cart icon with the number of items in the cart. Additionally, a responsive navigation menu should be present, featuring the main product categories and any other essential pages, such as "About Us" or "Contact."
2. Homepage: The homepage should feature a large, attention-grabbing banner or carousel showcasing popular or new products, special offers, or seasonal promotions. Below the banner, display a selection of featured products and categories, along with any relevant promotional material. Consider including a section for customer reviews or testimonials to build trust with potential buyers.
3. Product Listing Page: Design a clean and organized layout for the product listing page, displaying products in a grid format with clear images, product names, prices, and a brief description. Include pagination for easy browsing, as well as filtering and sorting options to help users find what they're looking for quickly.
4. Product Detail Page: The product detail page should include high-quality images of the product, a clear title, price, and availability information. Provide a detailed description, specifications, and any additional product information. Include an "Add to Cart" button, and display related products or upsell items to encourage additional purchases.
5. Shopping Cart Page: Create a clear and organized layout for the shopping cart page, displaying the selected products with images, names, prices, and quantities. Allow users to update the quantity or remove items from their cart, and display the subtotal, shipping fees, taxes, and total amount. Include a "Proceed to Checkout" button, as well as options to continue shopping or save the cart for later.
6. Checkout Page: Design a simple and user-friendly checkout process, with clear input fields for shipping and billing information, as well as a summary of the order details. Offer options for guest checkout or user registration, and provide a clear indication of the payment process and security measures in place.
7. User Account Dashboard: Create an organized dashboard for registered users, displaying options to view and edit account information, manage shipping addresses, view order history, and access any other relevant features.
8. Footer: The footer section should include links to important pages, such as "Terms & Conditions," "Privacy Policy," and "Return Policy." Also, provide contact information, social media icons, and a newsletter signup form for users who want to stay updated on promotions and news.

By following this design structure, the Home Store & More e-commerce webstore will provide a visually appealing, user-friendly, and seamless browsing and shopping experience for users, ultimately driving conversions and sales.


Site Navigation:

<details>
<summary>Diagram </summary>

![Diagram](/static/assets/images/diagram.png)
</details>

<br>
Aquerium House website design templates:

<details>
<summary>About page </summary>

![About page](/static/assets/images/about-page.png)
</details>
<details>
<summary>Home page </summary>

![Home page](/static/assets/images/home-page.png)
</details>
<details>
<summary>Post detail page </summary>

![Post detail page](/static/assets/images/post-detail-page.png)
</details>
<details>
<summary>Pricing page </summary>

![Picing page](/static/assets/images/pricing-page.png)
</details>
<details>
<summary>Contact page </summary>

![Contact page](/static/assets/images/contact-page.png)
</details>
<details>
<summary>Book Now page </summary>

![Book Now page](/static/assets/images/booknow-page.png)
</details>
<details>
<summary>My Bookings page </summary>

![My Bookings page](/static/assets/images/bookings-page.png)
</details>
<details>
<summary>Edit Bookings page </summary>

![Edit Bookings page](/static/assets/images/edit-bookings-page.png)
</details>
<details>
<summary>Delete Bookings page </summary>

![Delete Bookings page](/static/assets/images/delete-bookings-page.png)
</details>
<details>
<summary>Create Post </summary>

![Create post page](/static/assets/images/create-post.png)
</details>
<details>
<summary>Edit Post </summary>

![Edit post page](/static/assets/images/edit-post.png)
</details>
<details>
<summary>Delete Post </summary>

![Delete post page](/static/assets/images/delete-post.png)
</details>
<details>
<summary>Logout page </summary>

![Logout page](/static/assets/images/logout-page.png)
</details>
<details>
<summary>Login page </summary>

![Login page](/static/assets/images/login-page.png)
</details>
<details>
<summary>Register page </summary>

![Register page](/static/assets/images/signup-page.png)
</details>

<br/>

[Back to the top](#table-of-contents)

### Color Scheme

A well-chosen color scheme for the Home Store & More e-commerce webstore will create a visually appealing and cohesive user experience. Here is a proposed color scheme for the website:

1. Primary Color - Dark Blue: #1D3557
- Use this color for important elements, such as the header, footer, and main navigation menu. Dark blue conveys trust, professionalism, and stability, making it a popular choice for e-commerce websites.

2. Secondary Color - Light Blue: #A8DADC

- Apply this color for accents, such as buttons, links, and other interactive elements. Light blue provides a pleasant contrast to the dark blue and is associated with calmness and reliability.

3. Tertiary Color - Orange: #E76F51

- Use this color sparingly for attention-grabbing elements, such as call-to-action buttons, sale tags, or promotion banners. Orange is an energetic and eye-catching color that can encourage users to take action.

4. Background Color - Light Gray: #F1FAEE

- Utilize this color for the main background of the website, as it provides a clean and neutral backdrop that allows other colors and content to stand out.

5. Text Color - Dark Gray: #333333

- Use this color for the majority of the text content on the website. Dark gray is an excellent choice for readability and contrasts well with the light gray background.

By implementing this color scheme, the Home Store & More e-commerce webstore will create a visually appealing and user-friendly experience for its visitors. These colors will work together to establish a professional and trustworthy appearance, which is essential for an e-commerce website.
<details>
<summary>Color palette generator </summary>

![Register page](/static/assets/images/color-palette-generator.png)
</details>

<br/>

### Functional Structure

**Home page (User's Blog):** The home page contains a posts, logo and an image that gives the user an idea of ​​the type of service provided. Under the nav menu in the center is the button to create post, a new user or login for an existing user, only existing users can create a post. Not registered user will redirect to registration page.
Registration and login are also available from the navigation bar.

**Create post page:** The create post page is only available to authenticated users.
The user is asked to fill out a form with the required fields - title, content, image, and an optional field - excerpt.
After filling out the form, the user is to submit button and than user will be redirected to the page of current user's blog.

**Post detail page:** The post detail page is accessed by clicking on a link thumbnail that represents the post on a website's homepage. Once on the post detail page, users can read the full text of the article and interact with associated media, such as images, likes and comments.

**Edit post page:** This page is available only to authenticated users and has the same functionality and form as the create post page, where users can update post details.

**Delete post page:** This page is only available to authenticated users and has the same functionality and form as the create, update post page, where the user can update the post details. The user has the ability to delete user's post by selecting the Delete button on the post page. After that, user will be redirected to the delete page where user needs to confirm user's intention. After successfully deleting the post, user will return to the user's blog page and receives a message at the top of the screen.
Also, if the user changes user's mind, user can return to the page by clicking on the go Back button.

**Pricing page:** The Pricing page provides information about all available Aquarium House services. User also can book necessary service straight from the Pricing page by clicking on the services price and the user will be redirected to creat booking form.

**Registration page:** The user must create an account to make a reservation, or create post.
To do this, user is asked to fill out a form on the page with the required fields: username and password. There is also an optional email field.

**Login page:** A username and password are required to log in existing users.
The user can use the navigation menu login button.
After a successful login, the user receives a message at the top of the screen and is redirected to the main page.

**Logout page:** Logging out of the account is done through the navbar menu, after which the user is redirected to the logout page where user must confirm his desire to log out of the account. After a successful logout, the user is returned to the main page and receives a message at the top of the screen.

**Booknow page:** The Booknow page is only available to authenticated users.
The user is asked to fill out a form with the required fields - name, service, time and date, and an optional field - phone, email.
After filling out the form, the user is redirected to the page of current bookings.

**My Bookings page:** Only authenticated users have access to the Booking page. The link to this page becomes accessible in the navigation menu once a user is authenticated. Booking page shows to user information about made bookings and contains Change button and Delete button for manage booking.

**Change booking page:** This page is available only to authenticated users and has the same functionality and form as the Booknow page, where users can change  booking details.

**Delete booking page:** This page is only available to authenticated users and has the same functionality and form as the Booknow page, where the user can change the booking details. The user has the ability to delete user's booking by selecting the Delete button on the Booking page. After that, user will be redirected to the delete page where user needs to confirm user's intention. After successfully deleting the booking, user will return to the Booking page and receives a message at the top of the screen.
Also, if the user changes user's mind, user can return to the page by clicking on the Back to my Bookings button.

**Contact page** The contact page contains a contact information, Google map, phone number and support email, photo shooting service and "Book Now" button.
The Book Now button is accessible for new user or login for an existing user, only existing users can book. Not registered user will redirect to message page with the message: "To make a reservation, please login, if youhave not created an account yet, then please sign up.
Registration and login are also available from the navigation bar.

**About page** The page is open for all users, and contains the description of the company.

**Footer** The footer contains logo, navbar, contact information, social media icons, copyright.

### 404 page

The 404 page is an essential part of any website, as it serves as the error page displayed when a user attempts to visit a non-existent URL or encounters a broken link. A well-designed 404 page can help retain users and guide them back to the main site, rather than losing them due to frustration or confusion.

- For the Home Store & More e-commerce webstore, the 404 page should include the following design elements and features:
  1. **Clear Error Message:** Display a prominent and clear error message indicating that the requested page could not be found (e.g., "Oops! Page Not Found" or "404 Error: Page Not Found").
   
  2. **Consistent Design:** Maintain consistency in design, typography, and color scheme with the rest of the website to ensure a cohesive user experience and reinforce branding.
   
  3. **Helpful Suggestions:** Offer helpful suggestions or tips for users to find what they are looking for, such as checking the entered URL for typos, using the search function, or browsing through the main product categories.
  
  4. **Navigation Options:** Provide clear and easy-to-find navigation options, such as a search bar, links to popular categories or pages, and a button or link to return to the homepage. This will help guide users back to the main site and encourage them to continue browsing.
  
  5. **Engaging Visuals:** Consider using engaging visuals or illustrations related to the 404 error to inject a sense of humor or lightheartedness into the page, helping to alleviate user frustration and create a positive impression.
  
  6. **Responsive Design:** Ensure that the 404 page is responsive and looks good on various devices and screen sizes.
   
By incorporating these design elements and features, the 404 page for the Home Store & More e-commerce webstore will not only inform users of the error but also help guide them back to the main site, improving user experience and reducing bounce rates.

### 403 page

The 403 page is an important component of a website, as it serves as the error page displayed when a user attempts to access a restricted or forbidden resource. A well-designed 403 page can inform users about the issue and guide them to appropriate actions, rather than leaving them confused or frustrated.

1. **Clear Error Message:** Display a prominent and clear error message indicating that the user does not have permission to access the requested resource (e.g., "Access Denied" or "403 Error: Forbidden").

2. **Consistent Design:** Maintain consistency in design, typography, and color scheme with the rest of the website to ensure a cohesive user experience and reinforce branding.

3. **Explanation:** Provide a brief explanation of why the user might be seeing the 403 error, such as not being logged in, not having the necessary permissions, or trying to access a restricted area.

4. **Actionable Steps:** Offer actionable steps that users can take to resolve the issue, such as logging in, registering for an account, or contacting support for assistance.

5. **Navigation Options:** Provide clear and easy-to-find navigation options, such as a search bar, links to popular categories or pages, and a button or link to return to the homepage. This will help guide users back to the main site and encourage them to continue browsing.

6. **Engaging Visuals:** Consider using engaging visuals or illustrations related to the 403 error to convey the message in a more approachable manner and create a positive impression.

7. **Responsive Design:** Ensure that the 403 page is responsive and looks good on various devices and screen sizes.

By incorporating these design elements and features, the 403 page for the Home Store & More e-commerce webstore will effectively inform users about the access issue and guide them to appropriate actions, improving user experience and maintaining a professional appearance.

### 500 page

The 500 page is a crucial component of a website, as it serves as the error page displayed when a server-side error occurs. A well-designed 500 page can inform users about the issue and reassure them that the problem is being addressed, rather than leaving them frustrated or confused.

1. **Clear Error Message:** Display a prominent and clear error message indicating that there has been a server-side error (e.g., "Oops! Something went wrong" or "500 Error: Internal Server Error").

2. **Consistent Design:** Maintain consistency in design, typography, and color scheme with the rest of the website to ensure a cohesive user experience and reinforce branding.

3. **Explanation:** Provide a brief explanation of the issue, informing users that the server encountered an error while processing their request.

4. **Reassurance:** Reassure users that the issue is temporary and that the website's team is aware of the problem and working to resolve it as soon as possible.

5. **Navigation Options:** Provide clear and easy-to-find navigation options, such as a search bar, links to popular categories or pages, and a button or link to return to the homepage. This will help guide users back to the main site and encourage them to continue browsing.

6. **Engaging Visuals:** Consider using engaging visuals or illustrations related to the 500 error to convey the message in a more approachable manner and create a positive impression.

7. **Contact Information:** Provide contact information or a link to the support page, encouraging users to report the issue if it persists or if they need further assistance.

8. **Responsive Design:** Ensure that the 500 page is responsive and looks good on various devices and screen sizes.

By incorporating these design elements and features, the 500 page for the Home Store & More e-commerce webstore will effectively inform users about the server-side issue, reassure them that the problem is being addressed, and guide them to appropriate actions or alternative options, improving user experience and maintaining a professional appearance.

[Back to the top](#table-of-contents)

## Wireframes

Wireframes are an essential part of the design process, as they help visualize the layout and structure of a website before development begins. They are typically low-fidelity, focusing on the placement and organization of elements, rather than visual design or colors.

Here is a structure for created wireframes for the Home Store & More webstore.
The wireframes were slightly modified during the actual creation of the project, 
e.g. with pages installed removed form for user convenience and better UX.

The wireframes can be seen below:

### For Desktop view

1. **Homepage:** Include a header with the logo, search bar, user account options, and navigation menu. Feature a large banner or carousel, followed by sections showcasing featured products, categories, and promotions. Optionally, include a section for customer testimonials or reviews.
<details>
<summary>See wireframe screenshot:</summary>

 ![Homepage](static/assets/images/wireframes/home-desktop.png)
</details>
<br>

2. **Product Listing Page:** Design a clean layout with a grid of products, including images, titles, prices, and brief descriptions. Add pagination, filtering, and sorting options for easy browsing.
<details>
<summary>See wireframe screenshot:</summary>

 ![Product Listing Page](static/assets/images/wireframes/product-listing-page-desktop.png)
</details>
<br>

3. **Product Detail Page:** Display high-quality product images, title, price, and availability information. Include a detailed description, specifications, and an "Add to Cart" button. Optionally, showcase related products or upsell items.
<details>
<summary>See wireframe screenshot:</summary>

 ![Product Detail Page](static/assets/images/wireframes/product-detail-page-desktop.png)
</details>
<br>

4. **Shopping Cart Page:** Present a clear layout of the selected products with images, titles, prices, and quantities. Allow users to update quantities or remove items, and display the subtotal, shipping fees, taxes, and total amount. Include a "Proceed to Checkout" button and options to continue shopping or save the cart for later.
<details>
<summary>See wireframe screenshot:</summary>

 ![Shopping Cart Page](static/assets/images/wireframes/shopping-cart-page-desktop.png)
</details>
<br>

5. **Checkout Page:** Design a simple and user-friendly checkout process with input fields for shipping and billing information and a summary of the order details. Offer guest checkout or user registration and provide clear indications of the payment process and security measures.
<details>
<summary>See wireframe screenshot:</summary>

 ![Checkout Page](static/assets/images/wireframes/checkout-page-desktop.png)
</details>
<br>

6. **User Account Dashboard:** Create a dashboard for registered users with options to view and edit account information, manage shipping addresses, view order history, and access other relevant features.
<details>
<summary>See wireframe screenshot:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/user-account-dashboard-desktop.png)
</details>
<br>

7. **Hire Page:** Design a page dedicated to offering professional services, such as interior design, furniture assembly, or home improvement consultations. Include the following sections:
<details>
<summary>See wireframe screenshot "Hire" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/hire-page-desktop.png)
</details>
<br>

a. **Service Categories:** Display a grid or list of the different services offered, along with a brief description and an eye-catching image or icon for each category.

b. **How It Works:** Describe the process for hiring professionals through the website, such as submitting a request, receiving quotes, selecting a service provider, and making payments. Use clear and concise steps with accompanying visuals.

c. **Testimonials and Reviews:** Showcase positive feedback from previous customers who have used the website's hiring services. This can help build trust and credibility with potential clients.

8. **Packages Page:** Design a page dedicated to showcasing pre-selected or custom package deals, such as furniture sets, home decor bundles, or appliance combinations. Include the following sections:

<details>
<summary>See wireframe screenshot "Packages" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/packages-page-desktop.png)
</details>
<br>

a. **Featured Packages:** Display a grid or list of the featured packages, including images, titles, descriptions, and prices. Highlight any discounts or special offers associated with these packages.

b. **Custom Packages:** Offer users the option to create their own custom packages by selecting products from different categories. Provide an interactive interface where users can add, remove, or modify items in their custom package and see the updated price.

c. **Why Choose Our Packages:** Emphasize the benefits of purchasing packages, such as discounted prices, cohesive design, or hassle-free shopping experience. Use clear messaging and visuals to communicate these advantages.

d. **Customer Testimonials:** Showcase positive feedback from customers who have purchased packages from the website. This can help build trust and encourage potential clients to explore package options.




9. **About Page:** Design a page that shares the story, mission, and values of the Home Store & More e-commerce webstore. Include the following sections:
<details>
<summary>See wireframe screenshot "About" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/about-page-desktop.png)
</details>
<br>
a. **Our Story:** Provide a brief history of the company, its founders, and its journey to becoming an e-commerce webstore. Use engaging storytelling to connect with users on a personal level.

b. **Mission and Values:** Clearly articulate the company's mission and core values, emphasizing its commitment to customer satisfaction, product quality, and social responsibility.

c. **Team:** Showcase the key members of the company, including their photos, names, titles, and a brief bio. This can help humanize the brand and create a sense of trust with users.

d. **Why Shop With Us:** Highlight the unique selling points of the Home Store & More webstore, such as a wide product selection, competitive prices, or exceptional customer service. Use visuals and clear messaging to communicate these advantages.

e. **Press and Awards:** Mention any press coverage, industry recognition, or awards the company has received. This can help build credibility and authority in the market.

f. **Community Involvement:** Showcase any charitable initiatives or community projects the company has been involved in, demonstrating its commitment to social responsibility.

8. **404, 403, and 500 Error Pages:** Design error pages that clearly communicate the issue, offer helpful suggestions or actionable steps, and provide navigation options to guide users back to the main site.
<details>
<summary>See wireframe screenshot:</summary>

 ![404, 403, and 500 Error Pages](static/assets/images/wireframes/404.png)
</details>
<br>

[Back to the top](#table-of-contents)

### For Mobile view and small screens


1. **Homepage:**
<details>
<summary>See wireframe screenshot:</summary>

 ![Homepage](static/assets/images/wireframes/home-mobile.png)
</details>
<br>

2. **Product Listing Page:** 
<details>
<summary>See wireframe screenshot:</summary>

 ![Product Listing Page](static/assets/images/wireframes/product-listing-page-mobile.png)
</details>
<br>

3. **Product Detail Page:**
<details>
<summary>See wireframe screenshot:</summary>

 ![Product Detail Page](static/assets/images/wireframes/product-detail-page-mobile.png)
</details>
<br>

4. **Shopping Cart Page:** 
<details>
<summary>See wireframe screenshot:</summary>

 ![Shopping Cart Page](static/assets/images/wireframes/shopping-cart-page-mobile.png)
</details>
<br>

5. **Checkout Page:** 
<details>
<summary>See wireframe screenshot:</summary>

 ![Checkout Page](static/assets/images/wireframes/checkout-page-mobile.png)
</details>
<br>

6. **User Account Dashboard:** 
<details>
<summary>See wireframe screenshot:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/user-account-dashboard-mobile.png)
</details>
<br>

7. **Hire Page:** 
<details>
<summary>See wireframe screenshot "Hire" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/hire-page-mobile.png)
</details>
<br>

8. **Packages Page:**
<details>
<summary>See wireframe screenshot "Packages" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/packages-page-mobile.png)
</details>
<br>

9. **About Page:** 
<details>
<summary>See wireframe screenshot "About" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/about-page-mobile.png)
</details>
<br>

10. **Testimonials** 
<details>
<summary>See wireframe screenshot "Testimonials" page:</summary>

 ![User Account Dashboard](static/assets/images/wireframes/testimonials-page-mobile.png)
</details>
<br>

11. **404, 403, and 500 Error Pages:** 
<details>
<summary>See wireframe screenshot:</summary>

 ![404, 403, and 500 Error Pages](static/assets/images/wireframes/404-mobile.png)
</details>
<br>

[Back to the top](#table-of-contents)

## Features

1. **User-friendly Interface:** My website boasts a clean, intuitive design that makes navigation a breeze, ensuring a seamless and enjoyable shopping experience.

2. **Comprehensive Product Catalog:** Browse our extensive range of innovative equipment and supplementary products, curated to enhance your home or event space.

3. **Secure E-commerce Platform:** Shop with confidence on our secure e-commerce platform, featuring encrypted payment processing and robust data protection measures.

4. **Customizable Packages:** Choose from our pre-designed packages or create a custom solution tailored to your specific needs, ensuring a personalized experience for every occasion.

5. **Informative Product Descriptions:** Access detailed product descriptions, specifications, and images to help you make informed purchasing decisions.

6. **Customer Testimonials:** Read reviews and testimonials from our satisfied customers, providing valuable insights into the quality of our products and services.

7. **Responsive Customer Support:** Connect with our dedicated customer support team, ready to assist you with any questions or concerns throughout your shopping journey.

8. **Worldwide Shipping:** Enjoy the convenience of our worldwide shipping options, ensuring timely delivery of your purchases no matter where you are located.

### Navbar

- **Home:** Click to return to the homepage at any time, providing a starting point for browsing our website and exploring our products and services.

- **Products:** Access our comprehensive product catalog, showcasing our innovative equipment and supplementary products designed to enhance your home or event space.

- **Packages:** Explore our pre-designed and custom package options, tailored to meet the unique needs of various occasions and celebrations.

- **Testimonials:** Read reviews and testimonials from our satisfied customers, offering valuable insights into the quality of our products and services.

- **Blog:** Visit our blog for expert advice, tips, and inspiration on how to make the most of our products and services in your home or event space.

- **Contact Us:** Reach out to our dedicated customer support team with any questions or concerns, or to request a custom package tailored to your specific needs.

- **My Account:** Log in or create an account to access your order history, manage your personal information, and track your orders with ease.

- **Shopping Cart:** View your selected items, manage your order, and proceed to our secure checkout process to complete your purchase.

- **Search:** Utilize our integrated search feature to quickly find products or content on our website, making your shopping experience more efficient and enjoyable.

---

Navigation bar for an unauthorized user:
<details>

![Main navigation](/static/assets/features/navbar.png)

</details>

---
Navigation bar for an authorized user, menu items My Bookings and Logout are available:
<details>

![Authenticated user's Navigation](/static/assets/features/logged-navbar.png)

</details>

---

### Home page

The Home Page of the PP5 E-Commerce website serves as the main entry point for users and provides an engaging and visually appealing overview of the site's features and offerings. Key elements of the Home Page include:

- **Header:** The header contains the website logo, navigation menu, and user authentication options (login, signup, and logout). It allows users to navigate the website easily and access various sections such as products, testimonials, equipment hire, and more.

- **Featured Products:** A showcase of selected products, highlighting popular or new items available in the store. This section helps draw users' attention to specific products and encourages them to explore the store's offerings.

- **Promotional Banners:** Eye-catching banners that display promotions, discounts, or special announcements. These banners help inform users of ongoing sales or events and can drive engagement with the website.

- **News & Updates:** This section highlights the latest news, updates, or blog posts related to the store or its products. Keeping users informed about the latest developments helps build trust and encourages repeat visits.

- **Testimonials:** A display of customer testimonials, showcasing positive experiences and feedback from satisfied customers. This section helps build credibility and trust in the store's products and services.

- **Footer:** The footer contains additional navigation links, contact information, and social media icons. It helps users find important information quickly and easily and allows them to connect with the store on various social platforms.

The Home Page is designed to provide a welcoming and informative experience for users, guiding them through the website and encouraging interaction with the store's products and services.

<details>

![Home page](/static/assets/features/home.png)

</details>

---
### Products page

- **Product Categories:** A list of organized product categories, allowing customers to easily navigate and browse our extensive range of innovative equipment and supplementary products.
- **Product Availability:** Essential information about product availability, ensuring customers have a clear understanding of the product in stock.
- **Add to Wishlist:** An option for customers to save the product to their wishlist for future reference, making it simple to return to items they are interested in.
- **Product Images:** High-quality images that showcase the product, allowing customers to view the item in detail and make informed purchasing decisions.
- **Price Details:** Display the current price of the product, as well as giving customers a clear overview of the item's cost.

The product page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide a comprehensive and engaging shopping experience, making it easy for customers to find, compare, and purchase the perfect products to enhance their home or event space:
<details>

![Products page](/static/assets/features/product-page.png)

</details>

---
### Products Detail page

- **Detailed Product Information:** Comprehensive product descriptions, specifications, and images, helping customers make informed purchasing decisions based on their needs and preferences.
- **Customer Reviews and Ratings:** Real-life experiences and ratings from customers who have purchased and used the products, offering valuable insights into the quality and performance of each item.
- **Add to Cart Button:** A prominent and easy-to-use button that allows customers to quickly add products to their shopping cart and continue browsing the website.
- **Add to Wishlist:** An option for customers to save the product to their wishlist for future reference, making it simple to return to items they are interested in.
- **Product Images:** High-quality images that showcase the product, allowing customers to view the item in detail and make informed purchasing decisions.
- **Product Availability:** Essential information about product availability, ensuring customers have a clear understanding of the product in stock.
- **Price Details:** Display the current price of the product, as well as giving customers a clear overview of the item's cost.

The product detail page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with all the information they need to make an informed purchasing decision, offering a comprehensive and engaging shopping experience:

<details>

![Product Detail page](/static/assets/features/product-detail-page.png)

</details>

---
### Wishlist page

- **Wishlist Feature:** An option for customers to save their favorite products for future reference, making it simple to return to items they are interested in.
- **User-friendly Interface:** An intuitive design that makes it easy for customers to view, manage, and interact with their saved items on the wishlist page.
- **Product Thumbnails:** Visual representations of saved products, complete with images, product names, and brief descriptions, allowing customers to quickly recognize and review their saved items.
- **Add to Cart Button:** A convenient button next to each product that enables customers to add items directly from their wishlist to their shopping cart, streamlining the purchasing process.
- **Remove from Wishlist:** An option for customers to remove items from their wishlist, decluttering the list and keeping it up-to-date with their current preferences.
- **Product Availability Indicator:** A clear indication of each product's availability status, helping customers decide when to proceed with their purchase.
- **Price Information:** Display the current price of each saved product, allowing customers to make informed purchasing decisions and keep track of any changes in pricing.
- **Mobile Compatibility:** A responsive design that ensures the wishlist page is accessible and user-friendly on various devices, such as smartphones and tablets, for a seamless browsing experience.

The wishlist page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide a convenient and personalized shopping experience, allowing customers to save, manage, and purchase their favorite products with ease:

<details>

![Wishlist page](/static/assets/features/wishlist.png)

</details>

---
### About page

- **Company Overview:** A detailed introduction to Home Store & More + Techno Tech Co. Ltd, highlighting our mission, values, and unique selling points.
- **Company History:** A timeline or narrative outlining the milestones and significant events in our company's journey since its inception, showcasing our growth and achievements.
- **Team Profiles:** An introduction to our experienced team members, highlighting their expertise and roles within the company, fostering trust and connection with our customers.
- **Core Values:** A presentation of our company's core values and principles, demonstrating our commitment to excellence, innovation, and customer satisfaction.
- **Customer Testimonials:** A curated selection of customer testimonials that emphasize the positive experiences and quality of our products and services.
- **Partners and Collaborators:** A showcase of our strategic partners and collaborators, emphasizing our commitment to working with leading industry professionals and organizations.
- **Sustainability and Social Responsibility:** Information about our company's efforts to promote sustainability and social responsibility through eco-friendly practices and community involvement.
- **Contact Information:** Clear and accessible contact information, including phone numbers, email addresses, and physical location, ensuring customers can easily reach out to us with any questions or concerns.

The About page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with a comprehensive understanding of our company's background, values, and team, fostering trust and showcasing our commitment to quality and customer satisfaction:


<details>

![About page](/static/assets/features/about.png)

</details>

---
### Testimonials page

- **Testimonial Collection:** A curated selection of customer testimonials, showcasing the positive experiences and satisfaction of our clients with our products and services.
- **Featured Testimonials:** A highlighted section displaying the most impactful or recent testimonials, emphasizing the quality of our products and services.
- **Photos Testimonials:** A collection of photos testimonials from satisfied customers, offering a more engaging and personal view of their experiences with our products and services.
- **Responsive Design:** A mobile-friendly design that ensures the testimonials page is accessible and user-friendly on various devices, such as smartphones and tablets, for a seamless browsing experience.

The Testimonials page of Home Store & More + Techno Tech Co. Ltd's website is designed to showcase the positive experiences and satisfaction of our clients, providing potential customers with valuable insights into the quality and performance of our products and services:

<details>

![Testimonials page](/static/assets/features/testimonials.png)

</details>

---
### Hire page

- **Service Overview:** A brief introduction to our equipment hire service, explaining the benefits and advantages of choosing Home Store & More + Techno Tech Co. Ltd for equipment rentals.

- **Equipment Categories:** A well-organized list of equipment categories available for hire, allowing customers to easily browse and find the specific items they need for their projects or events.

- **Featured Equipment:** A showcase of our most popular and in-demand equipment available for hire.


- **Booking Process:** A step-by-step guide explaining the booking process, from selecting equipment to finalizing the rental agreement, ensuring a smooth and efficient experience for our customers.

The Hire page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with all the information they need to make informed decisions about equipment rentals, ensuring a seamless and efficient booking experience.
<details>

![Hire page](/static/assets/features/hire.png)

</details>

---
### Packages page

- **Package Categories:** A list of organized package categories, allowing customers to easily navigate and browse our range of pre-designed and custom package options for various events and spaces.
- **Detailed Package Information:** Comprehensive descriptions of each package, including the included products, services, and any additional features, helping customers make informed decisions based on their needs and preferences.
- **Package Pricing:** Clear and transparent pricing information for each package, including any discounts or promotions, giving customers a clear overview of the costs involved.
- **Customization Options:** An overview of available customization options for each package, allowing customers to tailor packages to suit their unique requirements and preferences.

The Packages page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with a comprehensive overview of our available package options and the benefits of choosing a package for their event or space, making it easy for them to find, compare, and purchase the perfect package for their needs.

<details>

![Packages page](/static/assets/features/packages.png)

</details>

---
### Footer

- **Company Information:** A brief introduction to Home Store & More + Techno Tech Co. Ltd, including our mission, values, and contact details, giving customers an overview of our company and easy access to our contact information.
- **Social Media Icons:** Prominent icons linking to our company's social media profiles, encouraging customers to connect with us on platforms like Facebook, Instagram, Twitter, and LinkedIn.
- **Newsletter Subscription:** An option for visitors to subscribe to our email newsletter, allowing them to stay updated on the latest news, promotions, and product releases from Home Store & More + Techno Tech Co. Ltd.
- **Terms & Conditions:** A link to our website's terms and conditions, providing customers with essential information about the use of our website and our services.
- **Privacy Policy:** A link to our privacy policy, outlining how we collect, use, and protect customer data, ensuring transparency and compliance with data protection regulations.
- **Site Map:** A comprehensive site map, allowing customers to easily navigate our website and find the information they need.

The footer of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with easy access to important information and resources, ensuring a seamless and user-friendly browsing experience.
<details>

![Footer](/static/assets/features/footer.png)

</details>

---
### Basket page

- **Basket Overview:** A clear and detailed display of all the items added to the shopping cart, including product names, images, quantities, and prices, allowing customers to review their selections before proceeding to checkout.
- **Edit Cart Functionality:** Options for customers to easily update the quantities or remove items from their cart, ensuring they have full control over their selections.
Subtotal and Total Calculation: Automatic calculation of the subtotal, shipping fees, taxes, and total cost, giving customers a clear overview of their order's total cost.

- **Secure Checkout Button:** A prominent and secure checkout button, directing customers to the payment process and ensuring a seamless and secure transaction.

- **Continue Shopping Button:** An easy-to-use button that allows customers to return to the website and continue browsing products without losing their cart selections.

- **Guest Checkout Option:** A feature that allows customers to proceed with the checkout process without creating an account, offering a faster and more convenient option for one-time purchases.

- **Sign In/Create Account:** A prompt for returning customers to sign in to their accounts for a faster checkout experience, as well as an option for new customers to create an account for future convenience and access to exclusive offers and promotions.

The Basket page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with a comprehensive and user-friendly overview of their cart selections and the associated costs, ensuring a seamless and efficient checkout process:

<details>

![Basket page](/static/assets/features/basket.png)

</details>

---
### Checkout page

- **Secure Checkout:** A secure and encrypted checkout process that ensures the safety and privacy of customer information, including personal details, shipping addresses, and payment information.

- **Order Summary:** A clear and detailed summary of the customer's order, including product names, images, quantities, prices, and 
allowing for a final review before submitting the order.

- **Shipping Address Form:** A simple and user-friendly form for customers to enter their shipping address, with options to save the address for future orders or choose from previously saved addresses.

- **Billing Address Form:** A separate form for customers to enter their billing address, with an option to use the same address as the shipping address for convenience.

- **Payment Methods:** A display of available payment methods, such as credit cards secure payment gateway.

- **Payment Information Input:** A secure form for customers to enter their payment information, with fields for credit card numbers, expiration dates, and CVV codes.

- **Order Confirmation:** A clear and concise order confirmation message, displaying the customer's order number and a summary of their purchase.

- **Email Confirmation:** An automated email sent to the customer upon successful completion of the order, containing their order details, shipping information.

The Checkout page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with a secure, efficient, and user-friendly experience when completing their purchase, ensuring a seamless and satisfying shopping experience.

<details>

![Checkout page](/static/assets/features/checkout.png)

</details>

---
### Sign up page

- **User-friendly Registration Form:** A simple and easy-to-use form for customers to enter their personal information, including name, email address, and password, streamlining the account creation process.

- **Email Verification:** An email verification step to ensure the authenticity of the user's email address, enhancing account security and preventing spam or unauthorized sign-ups.

- **Password Strength Indicator:** A visual indicator displaying the strength of the entered password, encouraging customers to create strong and secure passwords for their accounts.

- **Sign In Option for Existing Users:** A prompt for existing customers to sign in to their accounts, providing a seamless experience for those who already have an account with Home Store & More + Techno Tech Co. Ltd.

- **Responsive Design:** A mobile-friendly design that ensures the sign-up page is accessible and user-friendly on various devices, such as smartphones and tablets, for a seamless browsing experience.

The Sign Up page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with a secure, efficient, and user-friendly experience when creating their accounts, ensuring a seamless and enjoyable shopping experience:

<details>

![Sign up page](/static/assets/features/signup.png)

</details>

---

### Login page

- **User-friendly Login Form:** A simple and easy-to-use form for customers to enter their email address and password, streamlining the login process and providing quick access to their accounts.

- **Remember Me Checkbox:** An optional checkbox for customers to stay signed in, offering convenience for future visits to the website.

- **Forgot Password Link:** A helpful link for customers who have forgotten their password, guiding them through the password reset process and ensuring account security.

- **Responsive Design:** A mobile-friendly design that ensures the login page is accessible and user-friendly on various devices, such as smartphones and tablets, for a seamless browsing experience.

- **Login Error Messages:** Clear and helpful error messages displayed in case of incorrect email address or password, guiding customers to correct their input and successfully log in.

- **Secure Login Process:** A secure and encrypted login process that ensures the safety and privacy of customer information, including email addresses and passwords.

The Login page of Home Store & More + Techno Tech Co. Ltd's website is designed to provide customers with a secure, efficient, and user-friendly experience when accessing their accounts, ensuring a seamless and enjoyable shopping experience.

<details>

![Sign in page](/static/assets/features/login.png)

</details>

---

### Responsive design

Key features of responsive design include:

- **Fluid Grid Layout:** A flexible layout system that uses relative units (e.g., percentages) instead of fixed units (e.g., pixels) to define the width and height of elements, ensuring that the layout adjusts according to the screen size.

- **Flexible Images and Media:** Images, videos, and other media elements are set to automatically scale and resize according to the screen's dimensions, preventing distortion or overflow.

- **CSS Media Queries:** Media queries allow developers to apply different CSS styles based on the device's characteristics, such as screen size, resolution, and orientation. This enables the creation of device-specific designs that adapt to different viewing conditions.

- **Mobile-first Approach:** A design strategy that prioritizes the development of mobile layouts before scaling up to larger screens, ensuring that the user experience is optimized for mobile devices.

- **Touch-friendly Navigation:** User interface elements, such as buttons and menus, are designed to be easily accessible and navigable on touch-screen devices.

- **Optimized Performance:** Responsive designs often include techniques for improving website performance, such as image optimization, minification of CSS and JavaScript files, and lazy loading of assets, ensuring faster load times on mobile devices.

- **Seamless Content Display:** Content is organized and displayed in a way that maintains readability and usability across different devices, often using techniques such as collapsible menus, accordions, and content prioritization.

- **Cross-browser Compatibility:** Responsive designs are tested and optimized for compatibility across various web browsers, ensuring a consistent user experience.

- **Accessibility:** A responsive design should also consider accessibility guidelines and best practices, such as proper use of HTML tags, color contrast, and keyboard navigation, ensuring that the website is usable for people with disabilities.

Responsive design has become an essential aspect of modern web development, as it ensures that websites and applications are easily accessible and provide a consistent user experience across a wide range of devices.

---

### Database Schema

A database schema is a blueprint or structure that defines how data is organized in a database. It includes tables, fields, data types, relationships, and constraints that determine how the data is stored, related, and manipulated. Below is a basic example of a database schema for an e-commerce website like the one I mentioned earlier:

**Users Table:**
- user_id (Primary Key, Integer, Auto-increment)
- first_name (Varchar)
- last_name (Varchar)
- email (Varchar, Unique)
- password_hash (Varchar)
- created_at (Timestamp)
- updated_at (Timestamp)

**Products Table:**
- product_id (Primary Key, Integer, Auto-increment)
- product_name (Varchar)
- description (Text)
- price (Decimal)
- image_url (Varchar)
- stock (Integer)
- category_id (Foreign Key, Integer)
- created_at (Timestamp)
- updated_at (Timestamp)

**Categories Table:**
- category_id (Primary Key, Integer, Auto-increment)
- category_name (Varchar)
- created_at (Timestamp)
- updated_at (Timestamp)

**Orders Table:**
- order_id (Primary Key, Integer, Auto-increment)
- user_id (Foreign Key, Integer)
- order_status (Varchar)
- total_price (Decimal)
- created_at (Timestamp)
- updated_at (Timestamp)

**Order_Items Table:**
- order_item_id (Primary Key, Integer, Auto-increment)
- order_id (Foreign Key, Integer)
- product_id (Foreign Key, Integer)
- quantity (Integer)
- price (Decimal)
- created_at (Timestamp)
- updated_at (Timestamp)

**Addresses Table:**
- address_id (Primary Key, Integer, Auto-increment)
- user_id (Foreign Key, Integer)
- street (Varchar)
- city (Varchar)
- state (Varchar)
- zip_code (Varchar)
- country (Varchar)
- created_at (Timestamp)
- updated_at (Timestamp)

**Wishlist Table:**
- wishlist_id (Primary Key, Integer, Auto-increment)
- user_id (Foreign Key, Integer)
- product_id (Foreign Key, Integer)
- created_at (Timestamp)
- updated_at (Timestamp)

**About_Content Table:**
- about_id (Primary Key, Integer, Auto-increment)
- title (Varchar)
- content (Text)
- image_url (Varchar, Nullable)
- display_order (Integer)
- created_at (Timestamp)
- updated_at (Timestamp)

**Testimonials Table:**
- testimonial_id (Primary Key, Integer, Auto-increment)
- user_id (Foreign Key, Integer)
- content (Text)
- rating (Integer)
- created_at (Timestamp)
- updated_at (Timestamp)

**Equipment_Hire Table:**
- equipment_hire_id (Primary Key, Integer, Auto-increment)
- user_id (Foreign Key, Integer)
- package_id (Foreign Key, Integer)
- hire_start_date (Date)
- hire_end_date (Date)
- total_price (Decimal)
- created_at (Timestamp)
- updated_at (Timestamp)

**Contact_Submissions Table:**
- contact_id (Primary Key, Integer, Auto-increment)
- name (Varchar)
- email (Varchar)
- subject (Varchar)
- message (Text)
- status (Varchar, default: 'New') [e.g., New, In Progress, Closed]
- created_at (Timestamp)
- updated_at (Timestamp)

**Banners Table:**
- banner_id (Primary Key, Integer, Auto-increment)
- title (Varchar)
- description (Text, Nullable)
- image_url (Varchar)
- link (Varchar, Nullable)
- display_order (Integer)
- created_at (Timestamp)
- updated_at (Timestamp)

This is a simplified example of a database schema for an e-commerce website. Depending on the specific requirements and features of my website.

<details><summary>Table</summary>

![](/static/assets/images/database-table.png)
</details>

---

[Back to the top](#table-of-contents)

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Django
- SQLite (development) / PostgreSQL (production)
- Heroku for deployment

### Languages

- Python
- JavaScript
- HTML5
- CSS3

Installed Packages
---

**Package**          &         **Version**
------------------------- --------
- asgiref                   3.6.0
- boto3                     1.26.129
- botocore                  1.29.129
- cloudinary                1.32.0
- coverage                  7.2.5
- dj-database-url           0.5.0
- Django                    3.2
- django-allauth            0.41.0
- django-cloudinary-storage 0.3.0
- django-countries          7.2.1
- django-crispy-forms       1.14.0
- django-storages           1.13.2
- gunicorn                  20.1.0
- jmespath                  1.0.1
- oauthlib                  3.2.2
- Pillow                    9.5.0
- pip                       23.1.2
- psycopg2                  2.9.6
- python3-openid            3.2.0
- pytz                      2023.3
- requests-oauthlib         1.3.1
- s3transfer                0.6.1
- sqlparse                  0.4.4
- stripe                    5.4.0

### Frameworks

- [Django](https://www.djangoproject.com/): is a high-level Python web framework that enables rapid development of secure and maintainable websites.
<br>It follows the Model-View-Template (MVT) architectural pattern and promotes the DRY (Don't Repeat Yourself) principle,
 <br> which encourages the reuse of code and separation of concerns. Django comes with a built-in admin interface, 
 <br>a powerful ORM (Object-Relational Mapper), and support for various database systems, making it a popular choice for web developers. 
 <br>In this project, Django is used to create the backend, handle user authentication, manage the database, 
 <br>and serve the dynamic content for the PP5 House Stock E-Commerce website.

### Database

- [PostgreSQL](https://www.postgresql.org/): the database used to store All of the data.
<br>PostgreSQL is a powerful, open-source, object-relational database system that provides high performance, reliability, and extensibility. 
<br>It supports advanced data types, full-text search, and offers a vast array of features that make it suitable for various types of applications, 
<br>including web applications, data warehousing, and analytics. In this project, PostgreSQL is used as the production database to store all the data, 
<br>such as user information, products, orders, and other related information, ensuring data integrity and efficient data management for the PP5 E-Commerce website. 
<br>SQLite is used for the development environment, allowing for easy setup and testing during the development process.

### Cloud Hosting

- [Amazon Web Services](https://signin.aws.amazon.com/): AWS is a comprehensive cloud computing platform that offers a wide range of services, including computing power, storage, and databases. 
<br>AWS provides reliable, scalable, and cost-effective solutions for hosting web applications, making it a popular choice among developers and businesses. 
<br>In this project, AWS is utilized to host the static CSS files and media images for the PP5 E-Commerce website. By hosting these assets on a cloud platform like AWS, <br>the website benefits from increased performance, reduced latency, and enhanced scalability, ensuring a smooth and responsive user experience.

### Additional Media Hosting

- [Cloudinary](https://cloudinary.com/): the media hosting used to store some media due to extend more available storege for media. Cloudinary is a powerful, 
<br>feature-rich, and easy-to-use cloud-based media management platform. It offers an end-to-end solution for storing, transforming, and delivering images, 
<br>videos, and other media assets. Cloudinary enables developers to optimize media files for performance, automate image and video transformations, 
<br>and deliver content via a fast CDN (Content Delivery Network). In this project, Cloudinary is utilized for hosting and managing media assets, 
<br>such as product images, for the PP5 House Stock E-Commerce website. By leveraging Cloudinary, the website can efficiently serve optimized 
<br>and responsive media assets, ensuring a fast and visually appealing user experience.

### Tools

- [Google Fonts:](https://fonts.google.com/) Was used to to incorporate font styles.  
- [Font Awesome](https://fontawesome.com/): was used to create the icons used on the website.
- [Bootstrap](https://getbootstrap.com/) Was used to create the front-end design.
- [Gitpod:](https://Gitpod.io/) Gitpod was used as IDE to commit and push the project to GitHub.
- [GitHub:](https://github.com/) Was used as a version control system to manage the code
- [Figma:](https://www.figma.com/) Was used to create wireframes
- [TinyPNG:](https://www.figma.com/) Was used to reduce the size and weight of images and optimizing interaction with the site
- [Color Palette Generator:](https://mybrandnewlogo.com/color-palette-generator) Was used to select colors of the web site.
- [Am I Responsive](http://ami.responsivedesign.is/) to generate an image showcasing the website's responsiveness to different screen sizes
- [Pip3](https://pypi.org/project/pip/): is the package manager to install Python modules and libraries.
- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Requests for Python to understand.
- [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python.
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
- [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
- [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
- [Github Projects and Kanban board](https://github.com/users/SergiyKochenko/projects/6) was used to track the progress of the project in general and of every application in the project.
- [Free grammar checker](https://www.zoho.com/writer/free-grammar-checker.html)
- [Free formatter HTML](https://www.freeformatter.com/html-formatter.html#before-output): was used to format HTML5 code for the website.
- [Free cleancss CSS3](https://www.cleancss.com/css-beautify/): was used to format CSS3 code for the website.
- [Free black vercel](https://black.vercel.app/): was used to format python code for the website.

[Back to the top](#table-of-contents)

## Testing

### Bugs

#### Fixed Bugs

|  Bug  | Attached images  |  Solution  |Status   |
|--|--|--|--|
|  
Menu on mobile devices is positioned incorrectly | - | fixed CSS style   | fixed |
|Pricing form does not appear on the Pricing page  | - | fixed by passing form object to the pricing.html template , placing form tags in in the proper template pricing.html | fixed |
| In the Gitpod Environment the site works with full CSS style,  but on Heroku the site  and the admin page (/admin) comes up without CSS styling  | - | Set DEBUG variable to False and remove the DISABLE_COLLECTSTATIC variable | fixed |
| Function get_min_date isn't defined  | - | fixed by removing function from views.py file and placing function in the forms.py so the form can access that function | fixed  |
| When an invalid phone number is entered on the Booknow page, the form clears the fields and returns to its original state with no messages to the user. The Change Booking page also returns the form to its original state with pre-filled fields | - | Added regex validation for numeric input and displaying a message to the user | fixed  |
| Pricing elements on the Pricing page are not displayed correctly on mobile devices | - | added media queries rules for small screen devices  | fixed  |

<br/>

### Bug reports [bug reports](https://github.com/users/SergiyKochenko/projects/6)

<br/>

#### Unresolved Bugs

One bug known unresolved remaining
See bug report: [bug reports](https://github.com/users/SergiyKochenko/projects/6)
<details>
<summary>Create post page with the same title</summary>

![Create post page](/static/assets/bugs/create-post.png)

![Create post page](/static/assets/bugs/create-post2.png)

![Create post page](/static/assets/bugs/create-post1.png)

</details>

[Back to the top](#table-of-contents)

---

## Automated testing (Unit test)

- I have tested my web site, as experiment with automated testing. Currently I have covered 100% in total.
- See below the attached screen shots of the unit tests:

<details>
<summary>tests_admin.py</summary>

![Admin test](/static/assets/unit_tests/admin.png)

![Admin coverage](/static/assets/unit_tests/admin_coverage.png)

</details>
<details>
<summary>tests_models.py</summary>

![Models test](/static/assets/unit_tests/models.png)

![Models coverage](/static/assets/unit_tests/admin_coverage.png)

</details>
<details>
<summary>tests_views.py</summary>

![Views test](/static/assets/unit_tests/views.png)

![Views coverage](/static/assets/unit_tests/views_coverage.png)

</details>
<details>
<summary>Total test and coverage</summary>

![Total tests](/static/assets/unit_tests/total_tests.png)

![Total coverage](/static/assets/unit_tests/total_coverage.png)

</details>

<br/>

[Back to the top](#table-of-contents)

---

## Manual Testing

#### Device Testing

The Project was tested using a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard.
The following devices have been tested:

- Nest HubMax (Desktop)
- iPad Pro (Tablet)
- iPad Air (Tablet)
- iPad Mini (Tablet)
- Galaxy Tab S4 (Tablet)
- Nexus 7 (Mobile)
- Nokia N9 (Mobile)
- iPhone 12 Pro Max (Mobile)
- iPhone 5/SE (Mobile)
- iPhone 4 (Mobile)

#### Browsers Tested

Testing has been carried out on the  following browsers:

- Google Chrome
- Firefox
- Microsoft Edge
- Safari iOS

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience.
The available functionality and user experience is reflected in the table below.

| Goals/actions  | As a guest | As a logged user  | Result | Comment |
|--|:--:|:--:|:--:|--|
| User can use menu and navigating through pages | &check; | &check; | Pass | Click on menu item redirects to appropriate page |
| User can see the home page | &check; | &check; | Pass | |
| User can see the Pricing page | &check; |&check;  |  Pass| |
| User can see the Sign Up page | &check; |&check;  |  Pass| |
| User can see the Login page  | &check; |&check;  |  Pass| |
| User can see the Logout page  | &check; |&check;  |  Pass| |
| User can click the Book Now button  | &check; |&check;  |  Pass| Redirects to the page with a message that the user must register or log in for guest or shows up form for authorized user |
| User can see the Booknow page | &cross; | &check;  | Pass |A page is displayed with a message that the user must register or log in  |
| User can fill fields in the form the Booknow page | &cross; | &check;  | Pass |This page and form are available only to authorized users |
| User can see the Bookings page   | &cross; | &check;  | Pass | This page is available only to an authorized users|
| User can see the Change booking page  | &cross;  | &check;  | Pass | This page is available only to authorized users|
| User can edit booking in the form on the Change booking page  | &cross;  | &check;  | Pass |This page is available only to authorized users ||
| User can see the Delete booking page  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can see the  User's blog page  |  &check; | &check;  |Pass  |  |
| User can see the Create post  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can see the Delete post  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can see the  Update post  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can see the  attach image  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can like post and unlike  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| Admin can create service, edit and delete from admin site  |  &cross; | &check;  |Pass  | This page is available only for authorized admin |
| Admin can create post, update and delete from admin panel  |  &cross; | &check;  |Pass  | This page is available only for authorized admin |
| Admin can approve or delete comments from admin panel  |  &cross; | &check;  |Pass  | This page is available only for authorized admin |
| |

### Testing CRUD functionality

- Each of the features were tested multiple times to ensure that numerous new posts could be submitted, and that each post had the ability to be updated, edited and delete by the user that submitted it.
- If a post is submitted by another user, the edit/delete buttons do not appear on the page.
- Each of the features were tested multiple times to ensure that numerous new booking could be submitted, and that each booking had the ability to be updated, edited and delete by the user that submitted it.
- If a booking is submitted by another user, the particular ID booking list with edit/delete buttons do not appear on the page.

<br/>

[Back to the top](#table-of-contents)

## Validations

### HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.
There were errors and warnings in the reports about unclosed elements and tags, incorrect values ​​and types of elements, unnecessary trailing slashes. All errors and warnings have been fixed, the project's HTML code has been re-checked without errors.

<details><summary>base.html</summary>

![](/static/assets/validation/html/base.png)
</details>
<details><summary>about.html</summary>

![](/static/assets/validation/html/about.png)
</details>
<details><summary>bookings.html</summary>

![](/static/assets/validation/html/bookings.png)
</details>
<details><summary>booknow.html</summary>

![](/static/assets/validation/html/booknow.png)
</details>

<details><summary>change-booking.html</summary>

![](/static/assets/validation/html/change-booking.png)
</details>
<details><summary>contact.html</summary>

![](/static/assets/validation/html/contact.png)
</details>
<details><summary>create-post.html</summary>

![](/static/assets/validation/html/create-post.png)
</details>
<details><summary>delete_post.html</summary>

![](/static/assets/validation/html/delete_post.png)
</details>
<details><summary>delete-booking.html</summary>

![](static/assets/validation/html/delete-booking.png)
</details>
<details><summary>edit_post.html</summary>

![](/static/assets/validation/html/edit_post.png)
</details>
<details><summary>post_detail.html</summary>

![](static/assets/validation/html/post_detail.png)
</details>
<details><summary>pricing.html</summary>

![](/static/assets/validation/html/pricing.png)
</details>
<details><summary>usersblog.html</summary>

![](/static/assets/validation/html/usersblog.png)
</details>
<details><summary>login.html</summary>

![](/static/assets/validation/html/login.png)
</details>
<details><summary>logout.html</summary>

![](/static/assets/validation/html/logout.png)
</details>
<details><summary>signup.html</summary>

![](/static/assets/validation/html/signup.png)
</details>

---

### CSS Validation

The website CSS style has successfully passed the [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/).
![](static/assets/validation/css-validation.png)

---
<br/>

### Python Validation (PEP8)

All Python code was manually checked using [CI Python Linter](https://pep8ci.herokuapp.com/).
The Linter reports had messages about exceeding the string length of 79 characters. Testing did not reveal any errors.

<details><summary>urls.py</summary>

![](/static/assets/validation/pylint/urls.png)
</details>
<details><summary>models.py</summary>

![](/static/assets/validation/pylint/models.png)
</details>
<details><summary>forms.py</summary>

![](/static/assets/validation/pylint/forms.png)
</details>
<details><summary>views.py</summary>

![](/static/assets/validation/pylint/views.png)
</details>

---

### Lighthouse report

<br>

Desktop:

<details><summary>About page</summary>

![](/static/assets/lighthouse/about-desktop.png)
</details>
<details><summary>User's Blog page</summary>

![](/static/assets/lighthouse/usersblog-desktop.png)
</details>
<details><summary>Pricing page</summary>

![](/static/assets/lighthouse/pricing-desktop.png)
</details>
<details><summary>Contact page</summary>

![](/static/assets/lighthouse/contact-desktop.png)
</details>
<details><summary>Book Now page</summary>

![](/static/assets/lighthouse/booknow-desktop.png)
</details>
<details><summary>My Bookings page</summary>

![](/static/assets/lighthouse/mybookings-desktop.png)
</details>
<br>

Mobile:

<details><summary>About page</summary>

![](/static/assets/lighthouse/about-mobile.png)
</details>
<details><summary>User's Blog page</summary>

![](/static/assets/lighthouse/usersblog-mobile.png)
</details>
<details><summary>Pricing page</summary>

![](/static/assets/lighthouse/pricing-mobile.png)
</details>
<details><summary>Contact page</summary>

![](/static/assets/lighthouse/contact-mobile.png)
</details>
<details><summary>Book Now page</summary>

![](/static/assets/lighthouse/booknow-mobile.png)
</details>
<details><summary>My Bookings page</summary>

![](/static/assets/lighthouse/mybookings-mobile.png)
</details>

---
[Back to the top](#table-of-contents)

## Deployment

The project was developed using Gitpod, the project code is stored on GitHub, and then deployed to Heroku.
To deploy, follow these steps:

1. Log in to Heroku or create an account if required.
On the Welcome page in the top right corner click the button labeled 'New'.

2. From the drop-down menu select 'Create new app'.
Enter a preferred app name.
Select the relevant geographical region.
Click to 'Create App'.

3. Navigate to 'Settings' and scroll down to the 'Config Vars' section.
Click 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value. Then click 'Add'.
Add CLOUDINARY_URL, DATABASE_URL and SECRET_KEY. URL variable values ​​must be copied from your [CLOUDINARY](https://cloudinary.com/) account  and [ElephantSQL](https://www.elephantsql.com/) account.
To create a SECRET KEY, use the online service or come up with your own.

4. Click on the 'Deploy' tab.
Next to 'Deployment method' select 'GitHub'.
Connect the relevant GitHub repository.
Under 'Manual deploy' choose the correct branch and click 'Deploy Branch'.
Also you can select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub.

5. After successful deployment message in the page top right corner click the button labeled 'Open app' and you can access live app.

### Forking the GitHub Repository

To use this code and make changes without affecting the original code, it is possible to 'fork' the code on the GitHub repository through the following steps:

1. Create  or log into your GitHub account.
2. Go to the GitHub [repository](https://github.com/SergiyKochenko/portfolio-project-four).
3. Click the 'Fork' button in the upper right-hand corner of the page.
A copy of the repository will be available in your own repository.

### Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name choose button "Code",  click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open your development editor of choice and open a terminal window in a directory of your choice
5. Type *git clone*, and then paste the URL you copied in Step 3.

``> git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY``

Press Enter.

Your local clone will be created.

For more information follow this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop).

[Back to the top](#table-of-contents)

## Credits

### Code

The structure and the code of the project was based on two walkthroughs by the Code Institute:

- Hello Django - I created CRUD functionalities based on the examples of this walkthrough.
- From I think  therefore I blog -  I borrowed confirmation messages code and also followed the site deployment steps outlined here.

Date picker field and minimum date validator learned from [here](https://gist.github.com/stasyao/99376eb0cf0ad3599f9737c421b5210e#part_4).

[Official Django Documentation](https://docs.djangoproject.com/en/4.1/ref/) was researched for code expressions  and code functionalities.
Django [choices fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/).

Stack Overflow was used intensively for research into code functionalities and problem solving.

### Content

The site home page is taken from I think therefore I blog template. I slightly changed the look of the home page and tried to keep the rest of the pages in the same style.

### Media

Images were all open source and free to use from my owen collections, as I am aquarist my self and all the immages from my own aquarium :-)

### Contributing

This project is a personal portfolio project and is not open for contributions. However, you're welcome to explore the source code and use it as a reference or inspiration for your own projects.

### Inspiration

This project was inspired by the Hello Django project and the I Think Therefore I Blog project.
Website template from Aquarium community.

### Acknowledgment

- The Code Institute's Full Stack Software Development (eCommerce) Diploma program.
- Kerry Colledge for supporting all our group and for  individual support in all circumstances.
- Code Institute (especially the Django blog) which helped me to understand how it all comes together.
- The tutor support team at Code Institute for their support.
- To my friends who participated in testing my application.
- Martina Terlevic (my mentor), for helping me.
- Class mates for helping me.

[Back to the top](#table-of-contents)
