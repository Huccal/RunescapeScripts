package scripts.FmAPI;

import java.util.Random;

import org.tribot.api.General;
import org.tribot.api.Timing;
import org.tribot.api.types.generic.Condition;
import org.tribot.api.util.abc.ABCUtil;
import org.tribot.api2007.Game;
import org.tribot.api2007.Interfaces;
import org.tribot.api2007.Login;
import org.tribot.api2007.Options;
import org.tribot.api2007.Player;
import org.tribot.api2007.Skills;
import org.tribot.api2007.Skills.SKILLS;
import org.tribot.api2007.types.RSArea;
import org.tribot.api2007.types.RSInterface;
import org.tribot.api2007.types.RSTile;

import scripts.webwalker_logic.WebWalker;

public class FmGeneral {

	private static ABCUtil abc = new ABCUtil();

	public static int runAt = ABCGetRunAt();
	private static String currentStatus = "Starting Script";

	public static void sleepABC() {
		if (abc.shouldCheckTabs()) {
			FmGeneral.setStatus("Anti-ban");
			abc.checkTabs();
		} else {
			if (abc.shouldCheckXP()) {
				FmGeneral.setStatus("Anti-ban");
				abc.checkXP();
			} else {
				if (abc.shouldExamineEntity()) {
					FmGeneral.setStatus("Anti-ban");
					abc.examineEntity();
				} else {
					if (abc.shouldMoveMouse()) {
						FmGeneral.setStatus("Anti-ban");
						abc.moveMouse();
					} else {
						if (abc.shouldPickupMouse()) {
							FmGeneral.setStatus("Anti-ban");
							abc.pickupMouse();
						} else {
							if (abc.shouldRightClick()) {
								FmGeneral.setStatus("Anti-ban");
								abc.rightClick();
							} else {
								if (abc.shouldRotateCamera()) {
									FmGeneral.setStatus("Anti-ban");
									abc.rotateCamera();
								} else {
									if (abc.shouldLeaveGame()) {
										FmGeneral.setStatus("Anti-ban");
										abc.leaveGame();
									}
								}
							}
						}
					}
				}
			}
		}
	}

	public static int ABCGetRunAt() {
		return abc.generateRunActivation();
	}

	public static void activateRun() {
		Options.setRunOn(true);
		ABCGetRunAt();
	}

	public static boolean walkToArea(RSArea area) {
		RSTile tile = area.getRandomTile();
		if (Game.getRunEnergy() >= FmGeneral.runAt) {
			FmGeneral.activateRun();
		}
		if (WebWalker.walkTo(tile)) {
			Timing.waitCondition(new Condition() {
				@Override
				public boolean active() {
					General.sleep(100);
					return area.contains(Player.getPosition());
				}
			}, 2750);
		}
		return true;
	}

	public static boolean isInArea(RSArea area) {
		return area.contains(Player.getPosition());
	}

	public static boolean hasInterface(int id) {
		RSInterface rsi = Interfaces.get(id);
		if (rsi != null && !rsi.isHidden()) {
			return true;
		} else {
			return false;
		}
	}

	public static String getStatus() {
		return currentStatus;
	}

	public static void setStatus(String status) {
		currentStatus = status;
	}

	private final static Skills.SKILLS[] skills = { SKILLS.ATTACK, SKILLS.STRENGTH, SKILLS.DEFENCE, SKILLS.HITPOINTS,
			SKILLS.AGILITY, SKILLS.HERBLORE, SKILLS.RANGED, SKILLS.THIEVING, SKILLS.PRAYER, SKILLS.CRAFTING,
			SKILLS.MAGIC, SKILLS.FLETCHING, SKILLS.RUNECRAFTING, SKILLS.SLAYER, SKILLS.CONSTRUCTION, SKILLS.HUNTER,
			SKILLS.MINING, SKILLS.SMITHING, SKILLS.FISHING, SKILLS.COOKING, SKILLS.FIREMAKING, SKILLS.WOODCUTTING,
			SKILLS.FARMING };

	public static int getTotalXp() {
		int xp = 0;
		for (int i = 0; i < skills.length; i++) {
			xp += Skills.getXP(skills[i]);
		}
		return xp;
	}

	private final static int FREE_WORLDS[] = { 1, 9, 16, 26, 35, 82, 83, 84, 85, 93, 94 };
	private final static int MEMBER_WORLDS[] = { 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22,
			23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
			54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69, 70, 73, 74, 75, 76, 77, 78, 86, 87, 88, 89, 90,
			91 };


	public static int randomWorld(boolean members) {
		if (members) {
			return MEMBER_WORLDS[General.random(0, MEMBER_WORLDS.length-1)];
		} else {
			return FREE_WORLDS[General.random(0, FREE_WORLDS.length-1)];
		}
	}

	public static boolean login() {
		if (Login.getLoginState() == Login.STATE.INGAME) {
			return true;
		} else {
			if (Login.getLoginState() == Login.STATE.WELCOMESCREEN) {
				RSInterface loginButton = Interfaces.get(378, 17);
				if(loginButton!=null){
					loginButton.click("Play Runescape");
				} else {
					return false;
				}
			}
			return Login.getLoginState() == Login.STATE.INGAME;
		}
	}

}
