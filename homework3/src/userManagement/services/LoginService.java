package userManagement.services;

import java.util.ArrayList;
import java.util.List;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.Transaction;

import userManagement.util.HibernateUtil;
import userManagement.model.User;

public class LoginService {

    public boolean authenticateUser(String email, String password) {
        User user = getUserByUserEmail(email);
        if(user!=null && user.getEmail().equals(email) && user.getPassword().equals(password)){
            return true;
        }else{
            return false;
        }
    }

    public User getUserByUserEmail(String email) {
        Session session = HibernateUtil.openSession();
        Transaction tx = null;
        User user = null;
        try {
            tx = session.getTransaction();
            tx.begin();
            Query query = session.createQuery("from User where email='"+email+"'");
            user = (User)query.uniqueResult();
            tx.commit();
        } catch (Exception e) {
            if (tx != null) {
                tx.rollback();
            }
            e.printStackTrace();
        } finally {
            session.close();
        }
        return user;
    }

}
