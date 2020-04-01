package scripts.FmAPI;

import org.tribot.api.General;
import org.tribot.api.types.generic.Condition;
import org.tribot.api2007.Banking;
import org.tribot.api2007.Game;
import org.tribot.api2007.Interfaces;
import org.tribot.api2007.Inventory;
import org.tribot.api2007.Player;
import org.tribot.api2007.types.RSArea;
import org.tribot.api2007.types.RSInterfaceChild;
import org.tribot.api2007.Login;

/**
 * 
 * @author Final Caliber & Fmtrick
 *
 */

public class FmConditions
{
	public static final Condition IN_BANK_CONDITION = inBankCondition();
	public static final Condition IN_GAME_CONDITION = inWorldCondition();
	
	
	private static Condition inBankCondition()
	{
		return new Condition()
		{
			@Override
			public boolean active()
			{
				General.sleep(100);				
				return Banking.isInBank();
			}
			
		};
	}
	
	private static Condition inWorldCondition() {
		return new Condition() {

			@Override
			public boolean active() {
				General.sleep(100);
				return Login.getLoginState() == Login.STATE.INGAME;
			}
		};
	}
	
	public static Condition inAreaCondition(final RSArea area)
	{
		return new Condition()
		{
			@Override
			public boolean active()
			{	
				/*
				 * No sleep because this is being used for walking methods 
				 * (which have the sleep as a param)
				 */
				return area.contains(Player.getPosition());
			}
			
		};
	}
	
	public static Condition inventoryChanged(final int startingAmt)
	{
		return new Condition()
		{
			@Override
			public boolean active()
			{
				General.sleep(100);
				return Inventory.getAll().length != startingAmt;
			}	
		};
	}

	public static Condition uptextContains(String string) {
		return new Condition() {

			@Override
			public boolean active() {
				// TODO Auto-generated method stub
				return Game.getUptext().contains(string);
			}
			
		};
	}

	public static Condition interfaceUp(int dialogueMaster) {
		return new Condition() {

			@Override
			public boolean active() {
				return Interfaces.get(dialogueMaster)!=null;
			}
			
		};
	}

	public static Condition onWorldCondition(int worldNum) {
		return new Condition() {

			@Override
			public boolean active() {
				return Game.getCurrentWorld()==worldNum;
			}
		};
	}

	public static Condition interfaceNotUp(int hopperMaster) {
		return new Condition() {
			@Override
			public boolean active() {
				return Interfaces.get(hopperMaster)==null;
			}
		};
	}

	public static Condition interTextNotContains(int interfaceMaster, int interfaceChild, String string) {
		return new Condition() {

			@Override
			public boolean active() {
				RSInterfaceChild rsc = Interfaces.get(interfaceMaster,interfaceChild);
				if(rsc!=null){
					return rsc.getText() == string;
				} else {
					return false;
				}
			}
		};
	}
	
}