package userManagement.controller;
 
import java.io.IOException;
import javax.servlet.*;
import javax.servlet.http.*;
 
import userManagement.model.User;
import userManagement.services.LoginService;
 
 
public class LoginServlet extends HttpServlet {
	    public void doPost(HttpServletRequest request, HttpServletResponse response)
		    throws ServletException, IOException {
	 
		     String email = request.getParameter("email");   
		     String password = request.getParameter("pass");
		     LoginService loginService = new LoginService();
		     boolean result = loginService.authenticateUser(email, password);
		     User user = loginService.getUserByUserEmail(email);
		     if(result == true){
			request.getSession().setAttribute("user", user);      
			RequestDispatcher rs = request.getRequestDispatcher("index.html");
			rs.forward(request, response); 
		     }
		     else{
			RequestDispatcher rs = request.getRequestDispatcher("login.html");
			rs.forward(request, response); 
		     }
		}
}
