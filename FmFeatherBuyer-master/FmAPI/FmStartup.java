package scripts.FmAPI;

import java.awt.Point;

import org.tribot.api.input.Mouse;
import org.tribot.api2007.Camera;
import org.tribot.api2007.GameTab;
import org.tribot.api2007.Interfaces;
import org.tribot.api2007.Inventory;
import org.tribot.api2007.types.RSInterface;
import org.tribot.script.Script;

public class FmStartup {

	public static void setZoom() {
		GameTab.open(GameTab.TABS.OPTIONS);
		RSInterface topOptions = Interfaces.get(261, 1);
		if (topOptions != null) {
			RSInterface displayButton = topOptions.getChild(0);
			if (displayButton != null) {
				System.out.print(displayButton.getTextureID());
				if (displayButton.getTextureID() != 762) {
					displayButton.click("Display");
				}
				RSInterface zoomToggle = Interfaces.get(261, 4);
				if (zoomToggle != null) {
					if (Interfaces.get(261, 6).isHidden()) {
						zoomToggle.click("Select");
					}
				}
				RSInterface zoomSlider = Interfaces.get(261, 13);
				if (zoomSlider != null) {
					if (zoomSlider.getAbsolutePosition() != (new Point(601, 265))) {
						Mouse.drag(zoomSlider.getAbsolutePosition(), new Point(601, 265), 1);
					}
				}
			}
		}

	}

	public static void setCamera() {
		Camera.setCameraAngle(70);
	}

	public static void setShiftClick() {
		if (GameTab.getOpen() != GameTab.TABS.OPTIONS) {
			GameTab.open(GameTab.TABS.OPTIONS);
		}
		RSInterface topOptions = Interfaces.get(261, 1);
		if (topOptions != null) {
			RSInterface controlsButton = topOptions.getChild(7);
			if (controlsButton != null) {
				controlsButton.click("Controls");
				RSInterface toggleShiftClick = Interfaces.get(261, 65);
				if (!toggleShiftClick.isHidden() && toggleShiftClick != null) {
					if (toggleShiftClick.getTextureID() == 761) {
						toggleShiftClick.click("Toggle Shift Click Drop");
					}
				}
			}
		}
	}

	public static void setMiddleMouseCamera() {
		if (GameTab.getOpen() != GameTab.TABS.OPTIONS) {
			GameTab.open(GameTab.TABS.OPTIONS);
		}
		RSInterface topOptions = Interfaces.get(261, 1);
		if (topOptions != null) {
			RSInterface controlsButton = topOptions.getChild(7);
			if (controlsButton != null) {
				controlsButton.click("Controls");
				RSInterface toggleShiftClick = Interfaces.get(261, 59);
				if (!toggleShiftClick.isHidden() && toggleShiftClick != null) {
					if (toggleShiftClick.getTextureID() == 761) {
						toggleShiftClick.click("Toggle Mouse Camera");
					}
				}
			}
		}
	}

	public void run() {
		setZoom();
		setCamera();
		setShiftClick();
		Inventory.open();
	}

}
