package time;

import jason.asSemantics.DefaultInternalAction;
import jason.asSemantics.TransitionSystem;
import jason.asSemantics.Unifier;
import jason.asSyntax.StringTermImpl;
import jason.asSyntax.Term;

import java.text.SimpleDateFormat;
import java.util.Date;

public class check extends DefaultInternalAction {

    @Override
    public Object execute(TransitionSystem ts, Unifier un, Term[] args) throws Exception {
        String time = (new SimpleDateFormat("HH:mm:ss")).format(new Date());
        ts.getLogger().info("Check Time="+time);
        return un.unifies(args[0], new StringTermImpl(time));
    }
}

