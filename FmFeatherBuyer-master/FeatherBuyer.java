package scripts;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.io.IOException;
import java.net.URL;

import javax.imageio.ImageIO;

import java.awt.Font;

import org.tribot.api.DynamicClicking;
import org.tribot.api.General;
import org.tribot.api.Timing;
import org.tribot.api.types.generic.Condition;
import org.tribot.api2007.Camera;
import org.tribot.api2007.Interfaces;
import org.tribot.api2007.Inventory;
import org.tribot.api2007.Login;
import org.tribot.api2007.NPCs;
import org.tribot.api2007.Player;
import org.tribot.api2007.Walking;
import org.tribot.api2007.types.RSArea;
import org.tribot.api2007.types.RSInterfaceComponent;
import org.tribot.api2007.types.RSItem;
import org.tribot.api2007.types.RSNPC;
import org.tribot.api2007.types.RSTile;
import org.tribot.script.Script;
import org.tribot.script.ScriptManifest;
import org.tribot.script.interfaces.Painting;

import scripts.FmAPI.FmGeneral;
import scripts.FmAPI.FmHopper;
import scripts.FmAPI.FmStartup;

@ScriptManifest(authors = { "Fmtrick" }, category = "Money Making", name = "Trick's Feather Pack Buyer")

public class FeatherBuyer extends Script implements Painting {

	private final int FEATHER_PACK_ID = 11881;
	private RSTile shopCenterTile = new RSTile(3014, 3225, 0);
	private RSArea shopArea = new RSArea(shopCenterTile, 7);
	private State SCRIPT_STATE = getState();

	public enum State {
		TRADING, BUYING, OPENING, NO_COINS, WALK_TO_SHOP, LOGIN;
	}

	private State getState() {
		if (Login.getLoginState() == Login.STATE.INGAME) {
			if (haveCoins()) {
				if (atShop()) {
					if (havePacks()) {
						return State.OPENING;
					} else {
						if (FmGeneral.hasInterface(300)) {
							return State.BUYING;
						} else {
							return State.TRADING;
						}
					}
				} else {
					return State.WALK_TO_SHOP;
				}

			} else {
				return State.NO_COINS;
			}
		} else {
			return State.LOGIN;
		}
	}

	private boolean atShop() {
		return shopArea.contains(Player.getPosition());
	}

	private void worldHopper() {
		FmGeneral.setStatus("Hopping worlds");
		FmHopper.hop(FmGeneral.randomWorld(false));
	}

	public boolean buy() {
		RSInterface featherPack = Interfaces.get(300, 16, 9);
		RSInterface close = Interfaces.get(300, 11, 3);
		int waitTimer = 0;

		while (featherPack.getComponentStack() < 98) {
			FmGeneral.setStatus("Waiting for shop to restock (" + waitTimer + "/40)");
			sleep(500);
			waitTimer += 1;
			FmGeneral.sleepABC();
			if (waitTimer > 40) {
				if (close != null) {
					close.click("Close");
					worldHopper();
					break;
				}
			}
		}

		if (featherPack.getComponentStack() >= 98) {
			FmGeneral.setStatus("Purchasing 10 feathers");
			return featherPack != null && !featherPack.isHidden() && featherPack.click("Buy 10")
					&& close.click("Close");
		}

		return false;
	}

	private boolean haveCoins() {
		int goldAmount = Inventory.getCount("Coins");
		if (goldAmount < 2000) {
			println("Do not have enough money.");
			return false;
		} else {
			return true;
		}
	}

	private boolean havePacks() {
		sleep(750);
		RSItem[] packs = Inventory.find(FEATHER_PACK_ID);
		if (packs != null && packs.length > 0) {
			return true;
		} else if (packs.length < 1) {
			return false;
		}
		return false;
	}

	private boolean logout() {
		return Login.logout();
	}

	private Image getImage(String url) {
		try {
			return ImageIO.read(new URL(url));
		} catch (IOException e) {
			return null;
		}
	}

	private final Image img = getImage("https://i.imgur.com/AiiCLx5.png");
	Font font = new Font("Verdana", Font.PLAIN, 13);
	private static final long START_TIME = System.currentTimeMillis();

	@Override
	public void onPaint(Graphics g) {
		long timeRan = System.currentTimeMillis() - START_TIME;
		String status = FmGeneral.getStatus();
		g.setColor(new Color(1, 81, 102));
		g.setFont(font);
		Graphics2D gg = (Graphics2D) g;
		gg.drawImage(img, 0, 300, null);
		g.drawString(Timing.msToString(timeRan), 50, 375);
		g.drawString(status, 50, 400);

	}

	private boolean openPacks() {
		if (FmGeneral.hasInterface(300)) {
			RSInterfaceComponent close = Interfaces.get(300, 1).getChild(11);
			if (close != null) {
				close.click("Close");
			}
		}
		RSItem[] packs = Inventory.find(FEATHER_PACK_ID);
		println("Opening " + packs.length + " packs.");
		for (int i = 0; i < packs.length; i++) {
			packs[i].click("Open");
		}
		packs = Inventory.find(FEATHER_PACK_ID);
		if (havePacks()) {
			Timing.waitCondition(new Condition() {
				@Override
				public boolean active() {
					General.sleep(100);
					return havePacks() == false;
				}
			}, 2750);
		}
		return true;
	}

	public boolean trade() {
		RSNPC[] gerrant = NPCs.findNearest("Gerrant");
		if (gerrant != null && gerrant.length > 0) {
			if (gerrant[0].isOnScreen()) {
				if (DynamicClicking.clickRSNPC(gerrant[0], "Trade")) {
					Timing.waitCondition(new Condition() {
						@Override
						public boolean active() {
							General.sleep(100);
							return FmGeneral.hasInterface(300);
						}
					}, 6000);
				}
			} else {
				Camera.turnToTile(gerrant[0].getPosition());
				Walking.walkTo(gerrant[0].getPosition());
			}
		}
		return true;
	}

	private boolean walkToShop() {
		return FmGeneral.walkToArea(shopArea);
	}

	@Override
	public void run() {
		Login.login();
		FmStartup.setZoom();
		FmStartup.setCamera();
		FmStartup.setMiddleMouseCamera();
		loop: while (true) {
			SCRIPT_STATE = getState();
			switch (SCRIPT_STATE) {
			case BUYING:
				FmGeneral.setStatus("Buying feathers");
				buy();
				break;
			case WALK_TO_SHOP:
				FmGeneral.setStatus("Walking to shop");
				if (walkToShop()) {
					break;
				} else {
					println("failed to walk to shop. Ending script");
					break loop;
				}
			case NO_COINS:
				FmGeneral.setStatus("Out of cash, logging out");
				logout();
				break loop;
			case OPENING:
				FmGeneral.setStatus("Opening feather packs");
				if (openPacks()) {
					break;
				}
			case TRADING:
				FmGeneral.setStatus("C'mere, Gerrant");
				trade();
				break;
			case LOGIN:
				FmGeneral.login();
				break;
			}
			sleep(200);
		}
	}

}
