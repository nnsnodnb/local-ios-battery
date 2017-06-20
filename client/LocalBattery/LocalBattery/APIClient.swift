//
//  APIClient.swift
//  LocalBattery
//
//  Created by Oka Yuya on 2017/06/20.
//  Copyright © 2017年 Oka Yuya. All rights reserved.
//

import UIKit
import Alamofire

class APIClient: NSObject {

    class func request(_ url: String, method: HTTPMethod, parameter: Dictionary<String, Any>?, handler: @escaping ((DataResponse<String>) -> ())) {
        let header: [String: String] = ["Content-Type": "application/json"]
        
        let manager = Alamofire.SessionManager.default
        manager.session.configuration.timeoutIntervalForRequest = 15
        
        manager.request(url, method: method, parameters: parameter, encoding: JSONEncoding.default, headers: header)
            .responseString(completionHandler: { (response) in
                handler(response)
            })
    }
}
