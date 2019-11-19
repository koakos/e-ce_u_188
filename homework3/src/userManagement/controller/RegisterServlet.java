package userManagement.controller;
 
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
 
import userManagement.model.User;
import userManagement.services.RegisterService;


public class RegisterServlet extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
	     response.setContentType("text/html;charset=UTF-8");
	     PrintWriter out = response.getWriter();
	     String name = request.getParameter("name");
	     String email = request.getParameter("email");
	     String password = request.getParameter("pass");
	     User user = new User(name,email,password);
		     
	     try { 
		 RegisterService registerService = new RegisterService();
		 boolean result = registerService.register(user);      
		if(result){
			RequestDispatcher rs = request.getRequestDispatcher("index.html");
			rs.forward(request, response); 
		 }else{
		     out.println("<h1>Registration Failed</h1>");
		     out.println("To try again<a href=register.html>Click here</a>");
		 }
	     } finally {       
		 out.close();
	     }
	}
 
}

