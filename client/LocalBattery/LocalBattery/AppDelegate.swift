//
//  AppDelegate.swift
//  LocalBattery
//
//  Created by Oka Yuya on 2017/06/20.
//  Copyright © 2017年 Oka Yuya. All rights reserved.
//

import UIKit
import UserNotifications

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?


    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        setupNotificaiton(application)
        return true
    }

    func applicationWillResignActive(_ application: UIApplication) {
        
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        
    }

    func applicationWillTerminate(_ application: UIApplication) {
        
    }

    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
        let name: String = UIDevice.current.modelName
        let battery: String = UIDevice.current.battery
        let uuid: String = UIDevice.current.identifierForVendor!.uuidString
        let parameter: [String: String] = ["name": name,
                                           "battery": battery,
                                           "uuid": uuid]
        APIClient.request("http://192.168.11.9:8080/receive", method: .post, parameter: parameter) { (response) in
            if response.result.isSuccess {
                print(response.result.value!)
            }
        }
        completionHandler(.noData)
    }

    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        var token = String(format: "%@", deviceToken as CVarArg) as String
        let characterSet: CharacterSet = CharacterSet(charactersIn: "<>")
        token = token.trimmingCharacters(in: characterSet)
        token = token.replacingOccurrences(of: " ", with: "")

        let uuid: String = UIDevice.current.identifierForVendor!.uuidString
        let parameter: [String: String] = ["token": token,
                                           "uuid": uuid]
        APIClient.request("http://192.168.11.9:8080/token", method: .put, parameter: parameter) { (response) in
            if response.result.isSuccess {
                print(response.result.value!)
            }
        }
    }

    fileprivate func setupNotificaiton(_ application: UIApplication) {
        if #available(iOS 10.0, *) {
            UNUserNotificationCenter.current().requestAuthorization(options: [], completionHandler: { (grand, error) in
                guard error == nil else {
                    return
                }
                application.registerForRemoteNotifications()
            })
        } else {
            let settings = UIUserNotificationSettings(types: [],
                                                      categories: nil)
            application.registerUserNotificationSettings(settings)
            application.registerForRemoteNotifications()
        }
    }
}

